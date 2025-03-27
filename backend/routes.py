import json
import logging

from fastapi import APIRouter, HTTPException, status, Form, UploadFile
from celery.result import AsyncResult

from typing import Dict, Optional

from celery_tasks import analyze_fair
from resp_models import (
    OnlineResource,
    ResourceAcceptAssessment,
    TaskStatus,
    AssessmentResults,
    Feedback,
    Survey,
    ResourceAcceptFeedback,
)
from utils.network_utils import fetch_metadata_using_url
from utils.db_utils import (
    init_db,
    save_feedback,
    save_survey,
)

from config import setup_logging


# Define router to be imported
app_router = APIRouter()

init_db()

# Setup logging method
setup_logging()
logger = logging.getLogger("fastapi")


def __add_to_queue(metadata, user_tests: Optional[Dict] = None) -> str:
    """Method to create a task for FAIR analysis in the Celery Queue

    Args:
        file_type: type of file contents
        metadata: contents of the file
        user_tests: user-defined tests configuration

    Returns:
        task_id of the created Task
    """
    try:
        Task = analyze_fair.apply_async((metadata, user_tests), countdown=1)
        logger.info(f"Successfully created Task with ID: {Task.task_id}")
        return Task.task_id
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app_router.post(
    "/api/OnlineAnalyze",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ResourceAcceptAssessment,
)
async def handle_published(data: OnlineResource):
    """Endpoint to handle online published datasets from various repositories
    or any webpage with embedded metadata

    Args:
        data (OnlineResource): The url/doi of the datasets or any webpage with metadata

    Returns:
        ResourceAcceptResponse: Response indicating successful upload and task ID

    Raises:
        HTTPException: If there's an error processing the item, with status code 500
    """
    try:
        logger.info(f"Request initiated for online resource: {data.url}")
        # Using the given the url try to fetch metadata from different sources.
        success, metadata = await fetch_metadata_using_url(data.url.strip("/"))

        # Remove empty metadata sources
        for k in metadata.keys():
            if not metadata[k]:
                del metadata[k]

        if not success:
            logger.warning(
                f"Could not extract any related metadata from URL : {data.url}"
            )
            raise HTTPException(
                status_code=400,
                detail=f"Could not extract any related metadata from URL : {data.url}. Error: {metadata.get('error', 'Unknown error')}",
            )

        # Provide the extracted metadata from all sources to the celery task
        # And let it handle the merging of all metadata sources.

        # Add to processing queue
        task_id = __add_to_queue(
            metadata=metadata,
            user_tests=data.advancedTests,
        )

        return {
            "success": True,
            "comment": "Assessment is being processed",
            "task_id": task_id,
        }
    except Exception as e:
        logger.error(f"Error processing item: {data.url} Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app_router.post(
    "/api/OfflineAnalyze",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ResourceAcceptAssessment,
)
async def handle_unpublished(
    file: UploadFile,
    advanced_tests: str = Form(..., alias="advancedTests"),
):
    """Endpoint to handle offline file analysis

    Args:
        file (UploadFile): The uploaded file containing the resource metadata
        advanced_tests (str): JSON string of advanced test configurations

    Returns:
        ResourceAcceptResponse: Response indicating successful upload and task ID

    Raises:
        HTTPException: If there's an error processing the file, with status code 500
    """
    try:
        file_content = await file.read()
        file_content = file_content.decode("UTF-8")
        file_type = file.content_type

        logger.info(
            f"Request for Offline File Type {file_type} and file size: {file.size}"
        )

        # Load the user defined tests
        tests = json.loads(advanced_tests)

        task_id = __add_to_queue(
            metadata={"file": {"metadata": file_content, "source": file_type}},
            user_tests=tests,
        )
        return {
            "success": True,
            "comment": "File successfully uploaded",
            "task_id": task_id,
        }
    except Exception as e:
        logger.error(f"Error processing uploaded file: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app_router.get(
    "/api/Status/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskStatus
)
async def status_update(task_id: str):
    """Endpoint to check the status of assessment task

    Args:
        task_id (str): The ID of the task to check

    Returns:
        TaskStatus: Current status of the task and whether it's completed

    Raises:
        HTTPException: If the task is not found, with status code 404
    """
    try:
        res = AsyncResult(task_id)
        if not res:
            logger.warning(
                f"Status request sent for Task: {task_id} and task not found!"
            )
            raise HTTPException(status_code=404, detail="Task not found")
        logger.info(f"Status for task {task_id}: {res.status}")
        return {"success": res.ready(), "status": res.status}
    except Exception as e:
        logger.error(f"Error checking task status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app_router.get(
    "/api/Results/{task_id}",
    status_code=status.HTTP_200_OK,
    response_model=AssessmentResults,
)
async def get_results(task_id: str):
    """Endpoint to retrieve the results of the tasks

    Args:
        task_id (str): The ID of the task whose results are being requested

    Returns:
        AssessmentResults: The FAIR assessment results and task ID

    Raises:
        HTTPException: If the task is not found or still being processed
    """
    try:
        res = AsyncResult(task_id)
        if not res or not res.ready():
            logger.warning(f"Results requested for Task: {task_id} which are not ready")
            raise HTTPException(status_code=102, detail="Being Processed")
        return {"success": True, "fair_assessment": res.get(), "task_id": task_id}
    except Exception as e:
        logger.error(f"Error retrieving task results: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app_router.post(
    "/api/Feedback",
    status_code=status.HTTP_201_CREATED,
    response_model=ResourceAcceptFeedback,
)
async def feedback(feedback_data: Feedback):
    """Endpoint to handle user feedback

    Args:
        feedback_data (Feedback): The feedback data from the user

    Returns:
        ResourceAcceptFeedback: Response indicating successful feedback submission

    Raises:
        HTTPException: If there's an error saving the feedback
    """
    success = save_feedback(feedback_data)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save feedback",
        )
    return {"success": True}


@app_router.post(
    "/api/Survey",
    status_code=status.HTTP_201_CREATED,
    response_model=ResourceAcceptFeedback,
)
async def survey(survey_data: Survey):
    """Endpoint to handle user survey

    Args:
        survey_data (Survey): The survey data from the user

    Returns:
        ResourceAcceptFeedback: Response indicating successful survey submission

    Raises:
        HTTPException: If there's an error saving the survey
    """
    success = save_survey(survey_data)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save survey",
        )
    return {"success": True}

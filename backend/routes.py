import json
import logging
import log_config

import re

from fastapi import APIRouter, HTTPException, status, Form, UploadFile
from celery.result import AsyncResult

from typing import Dict

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
from utils import (
    fetch_zenodo_record,
    fetch_doi,
    fetch_dryad_record,
    init_db,
    save_feedback,
    save_survey,
)


# Define router to be imported
app_router = APIRouter()

init_db()

# Setup logging method
log_config.setup_logging()
logger = logging.getLogger("fastapi")


def __add_to_queue(file_type: str, file_content: str, user_tests: Dict) -> str:
    """Method to create a task for FAIR analysis in the Celery Queue

    Args:
        file_type: type of file contents
        file_size: size of the file (in Bytes)
        file_content: contents of the file

    Returns:
        task_id of the created Task
    """
    try:
        Task = analyze_fair.apply_async(
            (file_type, file_content, user_tests), countdown=1
        )
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
    """Endpoint to handle online published datasets from zenodo and dryad (doi)

    Args:
        item (OnlineResource): The url/ doi of the datasets

    Returns:
        ResourceAcceptResponse: Response indicating successful upload and task ID

    Raises:
        HTTPException: If there's an error processing the item, with status code 500
    """
    try:
        # make the get request based on either dryad or zenodo
        # Fow now only metadata and raise the request to perform analysis on the request
        logger.info(f"Request initiated for online resource: {data.url}")

        # Check if zenodo url or dryad record or doi
        pattern_zenodo = r"^(https?://)?zenodo\.org/records/\d+$"
        pattern_dryad = r"^(https?://)datadryad\.org/stash/dataset/doi:10\.\d+/dryad\.[a-zA-Z0-9-]+$"

        if re.match(pattern_zenodo, data.url):
            _record_num = data.url.split("/")[-1]
            res, zen_rec = await fetch_zenodo_record(_record_num)
            if not res:
                logger.warning(f"Could not resolve DOI for the url: {data.url}")
                raise HTTPException(
                    status_code=400,
                    detail=f"Could not resolve Zenodo Record {_record_num}",
                )
            file_content = json.dumps(zen_rec, separators=(",", ":"))
        elif re.match(pattern_dryad, data.url):
            doi = "/".join(data.url.split("/")[-2:])
            res, dry_rec = await fetch_dryad_record(doi)
            if not res:
                logger.warning(f"Could not resolve DOI for the url: {data.url}")
                raise HTTPException(
                    status_code=400,
                    detail=f"Could not resolve Zenodo Record {_record_num}",
                )
            file_content = json.dumps(dry_rec, separators=(",", ":"))
        else:
            # Send the doi to doi resolver to check for validity
            doi = "/".join(data.url.split("/")[-2:])
            logger.info(f"Processing DOI: {doi}")
            res, doi_resp = await fetch_doi(doi)
            if not res:
                logger.warning(f"Could not resolve DOI for the url: {data.url}")
                raise HTTPException(status_code=400, detail="Could not resolve DOI")
            if "zenodo" in data.url:
                _record_num = doi_resp["value"].split("/")[-1]
                res, zen_rec = await fetch_zenodo_record(_record_num)
                if not res:
                    logger.warning(f"Could not resolve DOI for the url: {data.url}")
                    raise HTTPException(
                        status_code=400,
                        detail=f"Could not resolve Zenodo Record {_record_num}",
                    )
                file_content = json.dumps(zen_rec, separators=(",", ":"))
            elif "dryad" in data.url:
                doi = "/".join(doi_resp["value"].split("/")[-2:])
                res, dry_rec = await fetch_dryad_record(doi)
                if not res:
                    logger.warning(f"Could not resolve DOI for the url: {data.url}")
                    raise HTTPException(
                        status_code=400,
                        detail=f"Could not resolve Zenodo Record {_record_num}",
                    )
                file_content = json.dumps(dry_rec, separators=(",", ":"))
        task_id = __add_to_queue(
            file_type="application/json",
            file_content=file_content,
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

        task_id = __add_to_queue(file_type, file_content, user_tests=tests)
        return {
            "success": True,
            "comment": "File succesfully uploaded",
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
                f"Status request sent for Task: {task_id} which is not found"
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
            logger.warning(
                f"Status request sent for Task: {task_id} which is not found"
            )
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
    # Save the feedback
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
    # Save the feedback
    success = save_survey(survey_data)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save survey",
        )
    return {"success": True}

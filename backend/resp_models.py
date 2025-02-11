from pydantic import BaseModel
from typing import Dict, Any, Optional


class Feedback(BaseModel):
    name: str
    email: Optional[str] = None
    feedback: str


##########################
#  Define Request Models #
##########################


class OnlineResource(BaseModel):
    url: str


##########################
# Define Response Models #
##########################


class ResourceAcceptFeedback(BaseModel):
    success: bool


class ResourceAcceptAssessment(BaseModel):
    task_id: str
    success: bool
    comment: str


class TaskStatus(BaseModel):
    success: bool
    status: str


class AssessmentResults(BaseModel):
    task_id: str
    success: bool
    # TODO: Define a detailed version of results after exporting one of the results
    fair_assessment: Dict[str, Any]

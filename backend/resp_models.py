from pydantic import BaseModel
from typing import Dict, Any, Optional, List


class Survey(BaseModel):
    easeOfUse: str
    recommendation: str
    fairFamiliarity: str
    priorUsage: str
    priorTools: str
    professionalStatus: str
    academicBG: str
    academicBgOther: Optional[str] = None
    usefulness: str
    fairRating: int
    usefulAspects: str
    futureUsage: str
    comments: Optional[str] = None


class Feedback(BaseModel):
    name: str
    email: Optional[str] = None
    feedback: str


##########################
#  Define Request Models #
##########################


class OnlineResource(BaseModel):
    url: str
    advancedTests: List[Dict]


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
    fair_assessment: Dict[str, Any]

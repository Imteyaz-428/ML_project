from fastapi import APIRouter, Depends
from models.user import Users
from utils.oauth2 import get_current_user
from crud.report import get_interview_report
from schemas.report import InterviewReportResponse

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)



@router.get(
    "/{interview_id}",
    response_model=InterviewReportResponse
)
def get_report(
    interview_id: int,
    current_user: Users = Depends(get_current_user)
):
    return get_interview_report(
        interview_id,
        current_user
    )
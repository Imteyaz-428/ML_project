from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.user import Users
from utils.oauth2 import get_current_user
from database.database import get_db
from crud.report import get_interview_report
from schemas.report import InterviewReportResponse

router = APIRouter(prefix="/report", tags=["Report"])


@router.get("/{interview_id}", response_model=InterviewReportResponse)
def get_report(
    interview_id: int,
    current_user: Users = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_interview_report(interview_id, current_user, db)

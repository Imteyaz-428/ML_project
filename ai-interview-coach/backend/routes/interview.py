from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.interview import InterviewCreate, InterviewListResponse
from crud.interview import create_interview, get_my_interviews, get_interview, get_all_interviews
from utils.oauth2 import get_current_user
from database.database import get_db
from models.user import Users

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


# ✅ FIX 4: /interviews route MUST come BEFORE /{interview_id}
# FastAPI matches routes top-to-bottom. Previously /{interview_id} was
# registered first, so GET /interview/interviews was captured by it and
# tried to cast "interviews" as an int → 422 error. The route was unreachable.
@router.get(
    "/interviews",
    response_model=List[InterviewListResponse]
)
def interviews(
    current_user: Users = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_all_interviews(current_user, db)


@router.post("/create")
def create(
    interview: InterviewCreate,
    current_user: Users = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_interview(interview, current_user, db)


@router.get("/my")
def my_interviews(
    current_user: Users = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_my_interviews(current_user, db)


# ✅ This wildcard route is now LAST — won't swallow /interviews anymore
@router.get("/{interview_id}")
def interview(
    interview_id: int,
    current_user: Users = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_interview(interview_id, current_user, db)

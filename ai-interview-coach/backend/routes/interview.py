from fastapi import APIRouter, Depends
from schemas.interview import InterviewCreate
from crud.interview import create_interview, get_my_interviews
from utils.oauth2 import get_current_user
from models.user import Users


router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)

@router.post("/create")
def create(interview: InterviewCreate,current_user: Users = Depends(get_current_user)):
    return create_interview(
        interview,
        current_user
    )
    
@router.get("/my")
def my_interviews(current_user: Users = Depends(get_current_user)):

    return get_my_interviews(current_user)
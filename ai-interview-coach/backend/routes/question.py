
from fastapi import APIRouter, Query
from pydantic import Field, EmailStr,field_validator
from schemas.user import User, User_update,UserResponse
from models.user import Users
from fastapi import Depends
from utils.oauth2 import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from crud.question import get_next_question, submit_answer
from schemas.question import QuestionAnswer

router = APIRouter(
    prefix="/question",
    tags=["question"]
)


@router.get("/next/{interview_id}")
def next_question(interview_id: int,current_user: Users = Depends(get_current_user)):
    
    return get_next_question(interview_id, current_user )

@router.post("/answer/{question_id}")
def answer_question(
    question_id: int,
    answer: QuestionAnswer,
    current_user: Users = Depends(get_current_user)
):

    return submit_answer(
        question_id,
        answer,
        current_user
    )
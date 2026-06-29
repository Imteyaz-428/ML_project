from fastapi import APIRouter, Depends
from utils.logger import logger
from models.user import Users
from utils.oauth2 import get_current_user

from crud.question import (
    get_next_question,
    submit_answer
)

from schemas.question import (
    QuestionAnswer,
    NextQuestionResponse
)

router = APIRouter(
    prefix="/question",
    tags=["Question"]
)


@router.get("/next/{interview_id}")
def next_question(
    interview_id: int,
    current_user: Users = Depends(get_current_user)
):

    return get_next_question(
        interview_id,
        current_user
    )


@router.post(
    "/submit/{question_id}",
    response_model=NextQuestionResponse
)
def submit(
    question_id: int,
    answer: QuestionAnswer,
    current_user: Users = Depends(get_current_user)
):
    logger.info("answer submitted start")
    return submit_answer(
        question_id,
        answer,
        current_user
    )
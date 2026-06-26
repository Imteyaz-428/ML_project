from models.question import Question
from database.database import session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from models.interview import Interview
from models.user import Users
from schemas.question import QuestionAnswer
from services.answer_evaluator import evaluate_answer
from crud.report import generate_final_report
from sqlalchemy.exc import SQLAlchemyError
import traceback

def create_questions(interview_id: int, questions: list[str]):
    try:
        for q in questions:
            question = Question(
                interview_id=interview_id,
                question=q
            )
            session.add(question)

        

        return {"message": "Questions created successfully"}


    except SQLAlchemyError as e:
        session.rollback()

        traceback.print_exc()
        print("SQL ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 
            
        
        
    
    
def get_next_question(interview_id: int,current_user: Users):
    #verify owernship
    interview = session.query( Interview).filter_by(id=interview_id,user_email=current_user.Email).first()
    
    if not interview:
        raise HTTPException(status_code=403, detail="You are not allowed to access this interview.")
    
    
    #first unaswered question
    question = (session.query(Question).filter(Question.interview_id == interview_id,Question.user_answer == None).first())
    
    if not question :
        raise HTTPException(status_code=404,detail="Interview completed.")
    return question







def submit_answer(
    question_id: int,
    answer: QuestionAnswer,
    current_user: Users
):

    try:

        # 1. Find Question
        question = session.query(Question).filter_by(
            id=question_id
        ).first()

        if not question:
            raise HTTPException(
                status_code=404,
                detail="Question not found."
            )

        # 2. Verify Interview Ownership
        interview = session.query(Interview).filter_by(
            id=question.interview_id,
            user_email=current_user.Email
        ).first()

        if not interview:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to answer this question."
            )

        # 3. Prevent answering twice
        if question.user_answer:
            raise HTTPException(
                status_code=400,
                detail="Question already answered."
            )

        # 4. Evaluate Answer using Gemini
        try:

            evaluation = evaluate_answer(
                question=question.question,
                user_answer=answer.user_answer,
                role=interview.role,
                difficulty=interview.difficulty
            )

        except Exception as e:

            if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):

                raise HTTPException(
                    status_code=429,
                    detail="Gemini API quota exceeded. Please try again later.")
                
            raise HTTPException(
                status_code=500,
                detail="Failed to evaluate answer.")

        # 5. Save Evaluation
        question.user_answer = answer.user_answer
        question.score = evaluation["score"]
        question.ai_feedback = evaluation["feedback"]
        question.correct_answer = evaluation["correct_answer"]
        question.strengths = evaluation["strengths"]
        question.improvements = evaluation["improvements"]

        # 6. Commit
        session.commit()

        # 7. Find Next Unanswered Question
        next_question = (
            session.query(Question)
            .filter(
                Question.interview_id == interview.id,
                Question.user_answer.is_(None)
            )
            .order_by(Question.id)
            .first()
        )
        if  next_question is None:
            report = generate_final_report(question.interview_id)
            return {
                "completed": True,
                "evaluation": evaluation,
                "report": report
            }

        # 8. Return Response
        return {
            "evaluation": evaluation,

            "next_question": (
                {
                    "id": next_question.id,
                    "question": next_question.question
                }
                if next_question
                else None
            ),

            "completed": next_question is None
        }

    except HTTPException:
        session.rollback()
        raise

    except Exception as e:
        session.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
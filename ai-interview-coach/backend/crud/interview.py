from fastapi import HTTPException

from database.database import session

from models.interview import Interview
from models.user import Users
from models.resume import Resume

from schemas.interview import InterviewCreate

from services.question_generator import generate_questions
from crud.question import create_questions


def create_interview(
    interview_data: InterviewCreate,
    current_user: Users
):

    # 1. Check if resume exists
    resume = session.query(Resume).filter_by(
        user_email=current_user.Email
    ).first()

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Please upload your resume first."
        )
    if not resume.parsed_data:
        raise HTTPException(
            status_code=400,
            detail="Resume analysis not found. Please upload your resume again."
        )
        
    parsed_resume = resume.parsed_data

    try:

        # 2. Create Interview
        interview = Interview(
            title=interview_data.title,
            company=interview_data.company,
            role=interview_data.role,
            difficulty=interview_data.difficulty,
            user_email=current_user.Email
        )

        session.add(interview)

        # 3. Generate interview.id without committing
        session.flush()

      

        try:

            questions = generate_questions(
                parsed_resume=parsed_resume,
                company=interview_data.company,
                role=interview_data.role,
                difficulty=interview_data.difficulty
            )

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=f"Question generation failed: {str(e)}"
            )

        # 5. Save Questions
        create_questions(
            interview.id,
            questions
        )

        # 6. Save everything
        session.commit()
        session.refresh(interview)

        return interview

    except Exception as e:

        session.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Interview creation failed: {str(e)}"
        )


def get_my_interviews(current_user: Users):

    return current_user.interviews
from fastapi import HTTPException

from database.database import session

from models.interview import Interview
from models.user import Users
from models.resume import Resume

from schemas.interview import InterviewCreate

from services.question_generator import generate_questions
from crud.question import create_questions
from utils.logger import logger

def create_interview(
    interview_data: InterviewCreate,
    current_user: Users
):
    logger.info(
        f"Creating interview for {current_user.Email}"
    )
    # 1. Check if resume exists
    resume = session.query(Resume).filter_by(
        user_email=current_user.Email
    ).first()

    if not resume:
        logger.warning(
            f"Resume not found for {current_user.Email}"
        )
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
            user_email=current_user.Email,
            interview_type=interview_data.interview_type,
            no_of_questions=interview_data.no_of_questions)

        session.add(interview)

        # 3. Generate interview.id without committing
        session.flush()

      

        try:
            logger.info("Generating interview questions")
            questions = generate_questions(
                parsed_resume=parsed_resume,
                company=interview_data.company,
                role=interview_data.role,
                difficulty=interview_data.difficulty,
                interview_type=interview_data.interview_type,
                no_of_questions=interview_data.no_of_questions
            )
            logger.info("Interview questions generated")

        except Exception as e:

            logger.exception(
                f"Question generation failed: {e}"
            )

            raise HTTPException(
                status_code=500,
                detail="Failed to generate interview questions."
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

    except HTTPException:

        session.rollback()

        raise

    except Exception as e:

        session.rollback()

        logger.exception(
            f"Interview creation failed: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to create interview."
        )

def get_my_interviews(current_user: Users):

    logger.info(
        f"Fetching interviews for {current_user.Email}"
    )

    return current_user.interviews


def get_interview(
    interview_id: int,
    current_user: Users
):
    interview = (
        session.query(Interview)
        .filter_by( id=interview_id,user_email=current_user.Email ).first())

    if not interview:
        logger.warning(
            f"Interview {interview_id} not found for {current_user.Email}"
        )
        raise HTTPException(
            status_code=404,
            detail="Interview not found."
        )
    logger.info(
        f"Interview {interview_id} fetched successfully"
    )
    return interview


from database.database import session
from models.interview import Interview
from models.report import InterviewReport

def get_all_interviews(current_user):

    interviews = (
        session.query(Interview)
        .filter(Interview.user_email == current_user.Email)
        .order_by(Interview.created_at.desc())
        .all()
    )

    result = []

    for interview in interviews:

        report = (
            session.query(InterviewReport)
            .filter_by(interview_id=interview.id)
            .first()
        )

        result.append({
            "id": interview.id,
            "company": interview.company,
            "role": interview.role,
            "difficulty": interview.difficulty,
            "overall_score": report.overall_score if report else None,
            "created_at": interview.created_at
        })

    return result
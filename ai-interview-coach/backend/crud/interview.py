from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.interview import Interview
from models.user      import Users
from models.resume    import Resume
from models.report    import InterviewReport

from schemas.interview import InterviewCreate

from services.question_generator import generate_questions
from crud.question import create_questions
from utils.logger  import logger


def create_interview(
    interview_data: InterviewCreate,
    current_user: Users,
    db: Session
):
    logger.info(f"Creating interview for {current_user.Email}")

    resume = db.query(Resume).filter_by(user_email=current_user.Email).first()

    if not resume:
        raise HTTPException(status_code=404, detail="Please upload your resume first.")

    if not resume.parsed_data:
        raise HTTPException(status_code=400, detail="Resume analysis not found. Please upload your resume again.")

    parsed_resume = resume.parsed_data

    try:
        interview = Interview(
            title            = interview_data.title,
            company          = interview_data.company,
            role             = interview_data.role,
            difficulty       = interview_data.difficulty,
            user_email       = current_user.Email,
            interview_type   = interview_data.interview_type,
            no_of_questions  = interview_data.no_of_questions
        )
        db.add(interview)
        db.flush()  # get interview.id without committing

        try:
            logger.info("Generating interview questions")
            questions = generate_questions(
                parsed_resume    = parsed_resume,
                company          = interview_data.company,
                role             = interview_data.role,
                difficulty       = interview_data.difficulty,
                interview_type   = interview_data.interview_type,
                no_of_questions  = interview_data.no_of_questions
            )
            logger.info("Interview questions generated")
        except Exception as e:
            logger.exception(f"Question generation failed: {e}")
            raise HTTPException(status_code=500, detail="Failed to generate interview questions.")

        create_questions(interview.id, questions, db)

        db.commit()
        db.refresh(interview)
        return interview

    except HTTPException:
        db.rollback()
        raise

    except Exception as e:
        db.rollback()
        logger.exception(f"Interview creation failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to create interview.")


def get_my_interviews(current_user: Users, db: Session):
    logger.info(f"Fetching interviews for {current_user.Email}")
    return current_user.interviews


def get_interview(interview_id: int, current_user: Users, db: Session):
    interview = (
        db.query(Interview)
        .filter_by(id=interview_id, user_email=current_user.Email)
        .first()
    )
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found.")

    return interview


def get_all_interviews(current_user: Users, db: Session):
    interviews = (
        db.query(Interview)
        .filter(Interview.user_email == current_user.Email)
        .order_by(Interview.created_at.desc())
        .all()
    )

    result = []
    for interview in interviews:
        report = (
            db.query(InterviewReport)
            .filter_by(interview_id=interview.id)
            .first()
        )
        result.append({
            "id":            interview.id,
            "company":       interview.company,
            "role":          interview.role,
            "difficulty":    interview.difficulty,
            "overall_score": report.overall_score if report else None,
            "created_at":    interview.created_at
        })

    return result

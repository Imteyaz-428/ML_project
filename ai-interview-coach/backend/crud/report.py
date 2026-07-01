from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user      import Users
from models.interview import Interview
from models.question  import Question
from models.report    import InterviewReport

from services.report_generator import generate_interview_report
from utils.logger import logger


def generate_final_report(interview_id: int, db: Session):
    logger.info(f"Generating report for interview {interview_id}")

    interview = db.query(Interview).filter_by(id=interview_id).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found.")

    questions = db.query(Question).filter_by(interview_id=interview_id).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found.")

    total_score   = sum(q.score or 0 for q in questions)
    overall_score = round(total_score / len(questions), 2)

    interview_data = {
        "company":       interview.company,
        "role":          interview.role,
        "difficulty":    interview.difficulty,
        "overall_score": overall_score,
        "questions": [
            {
                "question":     q.question,
                "score":        q.score,
                "feedback":     q.ai_feedback,
                "strengths":    q.strengths,
                "improvements": q.improvements
            }
            for q in questions
        ]
    }

    try:
        logger.info("Generating AI report")
        report = generate_interview_report(interview_data)
        logger.info("AI report generated successfully")
    except Exception as e:
        logger.exception(f"AI report generation failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate interview report.")

    existing_report = db.query(InterviewReport).filter_by(interview_id=interview_id).first()

    try:
        if existing_report:
            existing_report.overall_score       = overall_score
            existing_report.summary             = report["summary"]
            existing_report.overall_feedback    = report["overall_feedback"]
            existing_report.strong_domains      = report["strong_domains"]
            existing_report.weak_domains        = report["weak_domains"]
            existing_report.strengths           = report["strengths"]
            existing_report.weaknesses          = report["weaknesses"]
            existing_report.weak_skills         = report["weak_skills"]
            existing_report.recommendations     = report["recommendations"]
            existing_report.hiring_decision     = report["hiring_decision"]
            existing_report.hiring_justification= report["hiring_justification"]
            db.commit()
            db.refresh(existing_report)
            return existing_report

        interview_report = InterviewReport(
            interview_id        = interview_id,
            overall_score       = overall_score,
            summary             = report["summary"],
            overall_feedback    = report["overall_feedback"],
            strong_domains      = report["strong_domains"],
            weak_domains        = report["weak_domains"],
            strengths           = report["strengths"],
            weaknesses          = report["weaknesses"],
            weak_skills         = report["weak_skills"],
            recommendations     = report["recommendations"],
            hiring_decision     = report["hiring_decision"],
            hiring_justification= report["hiring_justification"]
        )
        db.add(interview_report)
        db.commit()
        db.refresh(interview_report)
        logger.info(f"Interview report created for interview {interview_id}")
        return interview_report

    except Exception as e:
        db.rollback()
        logger.exception(f"Database error while saving report: {e}")
        raise HTTPException(status_code=500, detail="Failed to save interview report.")


def get_interview_report(interview_id: int, current_user: Users, db: Session):
    logger.info(f"Fetching report for interview {interview_id}")

    interview = db.query(Interview).filter_by(
        id=interview_id, user_email=current_user.Email
    ).first()

    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found.")

    report = db.query(InterviewReport).filter_by(interview_id=interview_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Interview report not found.")

    return {
        "company":              interview.company,
        "role":                 interview.role,
        "difficulty":           interview.difficulty,
        "overall_score":        report.overall_score,
        "summary":              report.summary,
        "overall_feedback":     report.overall_feedback,
        "strong_domains":       report.strong_domains,
        "weak_domains":         report.weak_domains,
        "strengths":            report.strengths,
        "weaknesses":           report.weaknesses,
        "weak_skills":          report.weak_skills,
        "recommendations":      report.recommendations,
        "hiring_decision":      report.hiring_decision,
        "hiring_justification": report.hiring_justification,
        "created_at":           report.created_at
    }

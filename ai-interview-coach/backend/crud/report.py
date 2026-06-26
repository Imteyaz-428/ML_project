from fastapi import HTTPException
from models.user import Users
from database.database import session
from models.report import InterviewReport
from models.interview import Interview
from models.question import Question
from models.report import InterviewReport

from services.report_generator import generate_interview_report


def generate_final_report(interview_id: int):

    # Check Interview
    interview = session.query(Interview).filter_by(
        id=interview_id
    ).first()

    if not interview:
        raise HTTPException(
            status_code=404,
            detail="Interview not found."
        )

    # Get all questions
    questions = session.query(Question).filter_by(
        interview_id=interview_id
    ).all()

    if not questions:
        raise HTTPException(
            status_code=404,
            detail="No questions found."
        )

    # Calculate Overall Score
    total_score = sum(question.score for question in questions)

    overall_score = round(
        total_score / len(questions),
        2
    )

    # Prepare data for Gemini
    interview_data = {
        "company": interview.company,
        "role": interview.role,
        "difficulty": interview.difficulty,
        "overall_score": overall_score,
        "questions": []
    }

    for question in questions:

        interview_data["questions"].append({

            "question": question.question,

            "score": question.score,

            "feedback": question.feedback,

            "strengths": question.strengths,

            "improvements": question.improvements

        })

    # Generate AI Report
    try:

        report = generate_interview_report(
            interview_data
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Report generation failed: {str(e)}"
        )

    # Check if report already exists
    existing_report = session.query(
        InterviewReport
    ).filter_by(
        interview_id=interview_id
    ).first()

    if existing_report:

        existing_report.overall_score = overall_score
        existing_report.performance = report["performance"]
        existing_report.strengths = report["strengths"]
        existing_report.weaknesses = report["weaknesses"]
        existing_report.recommendation = report["recommendation"]
        existing_report.hiring_decision = report["hiring_decision"]

        session.commit()

        return existing_report

    # Create New Report
    interview_report = InterviewReport(

        interview_id=interview_id,

        overall_score=overall_score,

        performance=report["performance"],

        strengths=report["strengths"],

        weaknesses=report["weaknesses"],

        recommendation=report["recommendation"],

        hiring_decision=report["hiring_decision"]

    )

    session.add(interview_report)

    session.commit()

    session.refresh(interview_report)

    return interview_report




def get_interview_report(
    interview_id: int,
    current_user: Users
):

    # Check interview ownership
    interview = session.query(Interview).filter_by(
        id=interview_id,
        user_email=current_user.Email
    ).first()

    if not interview:
        raise HTTPException(
            status_code=404,
            detail="Interview not found."
        )

    # Fetch report
    report = session.query(InterviewReport).filter_by(
        interview_id=interview_id
    ).first()

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Interview report not found."
        )

    return report
import os
import shutil
import uuid
import traceback

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from models.user   import Users
from models.resume import Resume
from services.resume_parser  import extract_resume_text
from services.gemini_service import extract_resume_information


def upload_resume(resume: UploadFile, current_user: Users, db: Session):

    # ✅ FIX 5: Changed status_code from 400 → 422
    # The frontend checks for status 422 to show "Invalid file" error.
    # Returning 400 meant the frontend showed a generic error instead.
    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=422,
            detail="Only PDF files are allowed."
        )

    UPLOAD_DIR = "uploads/resumes"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    unique_filename = f"{uuid.uuid4()}_{resume.filename}"
    file_path       = os.path.join(UPLOAD_DIR, unique_filename)
    old_resume_path = None

    try:
        # Save uploaded PDF
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # Extract and parse resume text
        resume_text   = extract_resume_text(file_path)
        parsed_resume = extract_resume_information(resume_text)

        # Check if user already has a resume
        existing_resume = (
            db.query(Resume)
            .filter_by(user_email=current_user.Email)
            .first()
        )

        if existing_resume:
            old_resume_path             = existing_resume.resume_path
            existing_resume.resume_path = file_path
            existing_resume.resume_text = resume_text
            existing_resume.parsed_data = parsed_resume
        else:
            resume_data = Resume(
                user_email  = current_user.Email,
                resume_path = file_path,
                resume_text = resume_text,
                parsed_data = parsed_resume
            )
            db.add(resume_data)

        db.commit()

        # Delete old resume only after successful DB update
        if old_resume_path and os.path.exists(old_resume_path):
            os.remove(old_resume_path)

        return {"message": "Resume uploaded successfully"}

    except Exception as e:
        db.rollback()
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


def get_my_resume(current_user: Users, db: Session):
    resume = db.query(Resume).filter_by(user_email=current_user.Email).first()

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    return {
        "resume_path": resume.resume_path,
        "analysis":    resume.parsed_data
    }


def delete_resume(current_user: Users, db: Session):
    resume = db.query(Resume).filter_by(user_email=current_user.Email).first()

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    if os.path.exists(resume.resume_path):
        os.remove(resume.resume_path)

    db.delete(resume)
    db.commit()

    return {"message": "Resume deleted successfully"}

from fastapi import APIRouter, UploadFile, File, Depends
from models.user import Users
from utils.oauth2 import get_current_user
from crud.resume import ( upload_resume,get_my_resume, delete_resume)
from utils.logger import logger

router = APIRouter( prefix="/resume", tags=["Resume"])

@router.post("/upload")
def upload(
    resume: UploadFile = File(...), current_user: Users = Depends(get_current_user)):
    

    logger.info("Resume upload started")
    return upload_resume(
        resume,
        current_user
    )
    
    
@router.get("/me")
def get_resume(
    current_user: Users = Depends(get_current_user)):
    return get_my_resume(current_user)


@router.delete("/")
def delete(
    current_user: Users = Depends(get_current_user)):
    return delete_resume(current_user)
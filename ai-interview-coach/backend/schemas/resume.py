from pydantic import BaseModel
from datetime import datetime

class ResumeResponse(BaseModel):
    id: int
    resume_path: str
    uploaded_at: datetime

    class Config:
        from_attributes = True
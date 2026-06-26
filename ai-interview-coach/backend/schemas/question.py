from pydantic import BaseModel
from typing import Optional

class QuestionCreate(BaseModel):
    interview_id: int
    question: str
    

class QuestionAnswer(BaseModel):
    user_answer: str
    
    
class QuestionResponse(BaseModel):
    id: int
    question: str
    sscore: Optional[int] = None
    ai_feedback: Optional[str] = None
    class Config:
        from_attributes = True
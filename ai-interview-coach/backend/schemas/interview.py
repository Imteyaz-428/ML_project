from pydantic import BaseModel, Field
from typing import Annotated, Literal
from datetime import datetime
from typing import Optional

class InterviewCreate(BaseModel):

    title: Annotated[str, Field(max_length=100)]

    company: Annotated[str, Field(max_length=50)]

    role: Annotated[str, Field(max_length=50)]

    difficulty: Literal[
        "Easy",
        "Medium",
        "Hard"
    ]
    interview_type : str
    no_of_questions : int
    



class InterviewListResponse(BaseModel):
    id: int
    company: str
    role: str
    difficulty: str
    

    overall_score: Optional[float] = None
    created_at: datetime

    class Config:
        from_attributes = True
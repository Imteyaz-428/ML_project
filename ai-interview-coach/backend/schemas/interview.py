from pydantic import BaseModel, Field
from typing import Annotated, Literal

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
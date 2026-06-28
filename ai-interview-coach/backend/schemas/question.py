from pydantic import BaseModel
from typing import Optional,List

class QuestionCreate(BaseModel):
    interview_id: int
    question: str
    

class QuestionAnswer(BaseModel):
    user_answer: str
    
    


class QuestionResponse(BaseModel):

    id: int

    company: str

    role: str

    current_question: int

    total_questions: int

    category: str

    difficulty_tag: str

    question: str

    class Config:
        from_attributes = True
        


from typing import List

class EvaluationResponse(BaseModel):

    score: int

    feedback: str

    correct_answer: str

    strengths: List[str]

    improvements: List[str]
    
    
class NextQuestionResponse(BaseModel):

    evaluation: EvaluationResponse

    next_question: Optional[QuestionResponse] = None

    completed: bool

    report: Optional[dict] = None
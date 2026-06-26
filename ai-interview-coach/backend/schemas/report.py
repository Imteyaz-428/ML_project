from pydantic import BaseModel
from typing import List


class InterviewReportResponse(BaseModel):
    interview_id: int
    overall_score: float
    performance: str
    strengths: List[str]
    weaknesses: List[str]
    recommendation: str
    hiring_decision: str
    class Config:
        from_attributes = True
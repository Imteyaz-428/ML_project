from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime


class InterviewReportResponse(BaseModel):
    company: str
    role: str
    difficulty: str

    overall_score: float

    summary: str
    overall_feedback: str

    strong_domains: List[Dict]
    weak_domains: List[Dict]

    strengths: List[str]
    weaknesses: List[str]
    weak_skills: List[str]
    recommendations: List[str]

    hiring_decision: str
    hiring_justification: str

    created_at: datetime

    class Config:
        from_attributes = True
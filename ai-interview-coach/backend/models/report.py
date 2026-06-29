from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    DateTime,
    ForeignKey,
    JSON
)

from sqlalchemy.orm import relationship
from datetime import datetime
from models.user import Base


class InterviewReport(Base):

    __tablename__ = "interview_report"

    id = Column(
        Integer,
        primary_key=True
    )

    interview_id = Column(
        Integer,
        ForeignKey("interview_info.id"),
        unique=True,
        nullable=False
    )

    # Overall Interview Score
    overall_score = Column(Float)

    # Recruiter Summary
    summary = Column(Text)

    # Overall Performance Feedback
    overall_feedback = Column(Text)

    # Domains
    strong_domains = Column(JSON)
    weak_domains = Column(JSON)

    # Lists
    strengths = Column(JSON)
    weaknesses = Column(JSON)
    weak_skills = Column(JSON)
    recommendations = Column(JSON)

    # Hiring
    hiring_decision = Column(Text)
    hiring_justification = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    interview = relationship(
        "Interview",
        back_populates="report"
    )
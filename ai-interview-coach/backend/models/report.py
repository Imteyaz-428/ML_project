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

    overall_score = Column(Float)

    performance = Column(Text)
    strengths = Column( JSON)
    weaknesses = Column(JSON)

    recommendation = Column( Text)
    hiring_decision = Column( Text)
    created_at = Column( DateTime, default=datetime.utcnow)
    interview = relationship( "Interview", back_populates="report")
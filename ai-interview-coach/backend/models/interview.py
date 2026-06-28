from sqlalchemy import Integer, String,Column, Text

from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import DateTime,ForeignKey
from datetime import datetime
from models.user import Base


class Interview(Base) :
    __tablename__ = "interview_info"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    company = Column(String(50))
    role = Column(String(50))
    difficulty = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    user_email = Column(String(30),ForeignKey("user_info.Email"), nullable=False)
    interview_type = Column(String(30))
    no_of_questions = Column(Integer)
    user = relationship( "Users", back_populates="interviews")
    
    questions = relationship( "Question",back_populates="interview")
    report = relationship( "InterviewReport",back_populates="interview",uselist=False,cascade="all, delete-orphan")
    
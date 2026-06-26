from sqlalchemy import Integer, String,Column, Text, JSON

from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import DateTime,ForeignKey
from datetime import datetime
from models.user import Base


class Question(Base) :
    __tablename__ = "question_info"
    id = Column(Integer,primary_key=True)
    question = Column(Text)
    user_answer = Column(Text, nullable=True)
    ai_feedback = Column(Text, nullable=True)
    score = Column(Integer, nullable=True)
    created_at = Column(DateTime,default=datetime.utcnow)
    interview_id = Column(Integer, ForeignKey("interview_info.id"))
    correct_answer = Column(Text, nullable=True)
    strengths = Column(JSON, nullable=True)
    improvements = Column(JSON, nullable=True)
    interview = relationship( "Interview", back_populates="questions")
    
    

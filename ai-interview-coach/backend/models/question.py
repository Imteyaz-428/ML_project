from sqlalchemy import Integer, String, Column, Text, JSON, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from models.user import Base


from sqlalchemy import JSON

class Question(Base):
    __tablename__ = "question_info"

    id = Column(Integer, primary_key=True)

    question = Column(Text)

    category = Column(String(100))
    follow_up = Column(Text)
    expected_answer_points = Column(JSON)
    difficulty = Column(String(20))
    time_limit = Column(Integer)

    user_answer = Column(Text, nullable=True)
    ai_feedback = Column(Text, nullable=True)
    score = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    interview_id = Column(Integer, ForeignKey("interview_info.id"))

    correct_answer = Column(Text, nullable=True)
    strengths = Column(JSON, nullable=True)
    improvements = Column(JSON, nullable=True)

    interview = relationship("Interview", back_populates="questions")
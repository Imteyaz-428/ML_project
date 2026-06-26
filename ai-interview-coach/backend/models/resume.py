from sqlalchemy import Integer, String,Column, Text,JSON
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import DateTime,ForeignKey
from datetime import datetime
from models.user import Base



class Resume(Base):
    __tablename__ = "resume_info"
    id = Column(Integer, primary_key=True)
    user_email = Column(
        String(30),
        ForeignKey("user_info.Email"),
        nullable=False
    )
    resume_path = Column(String(100))
    resume_text = Column(Text)
    parsed_data = Column(JSON)
    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    user = relationship(
        "Users",
        back_populates="resumes"
    )
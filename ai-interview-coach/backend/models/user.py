from sqlalchemy import Integer, String,Column
from database.database import SessionLocal , engine
from sqlalchemy.orm import declarative_base, relationship


#base class
Base = declarative_base()

#Model
class Users(Base) :
    __tablename__ = "user_info"
    
    
    Email = Column(String(30), unique=True, nullable=False, primary_key=True)
    Name = Column(String(30))
    Age = Column(Integer)
    Gender = Column(String(10))
    Trade = Column(String(50))
    password = Column(String(255), nullable=False)
    interviews = relationship("Interview", back_populates="user",cascade="all, delete")
    resumes = relationship("Resume",back_populates="user",uselist=False)


#create engine 
Base.metadata.create_all(engine)

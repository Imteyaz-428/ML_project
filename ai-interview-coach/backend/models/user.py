from sqlalchemy import Integer, String,Column
from database.database import SessionLocal , engine
from sqlalchemy.orm import declarative_base

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
    password = Column(String(30))


#create engine 
Base.metadata.create_all(engine)

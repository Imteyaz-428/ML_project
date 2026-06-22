from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#database connection 
DATABASE_URL = "mysql+pymysql://interview:password123@localhost/user_db"

engine = create_engine(DATABASE_URL)

SessionLocal  = sessionmaker(
    autoflush= False,
    autocommit = False,
    bind = engine
)
session = SessionLocal()
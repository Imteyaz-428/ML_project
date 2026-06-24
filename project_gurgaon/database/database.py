from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# MySQL Uimport os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={
        "ssl": {}
    }
)
# Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Class
Base = declarative_base()


# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
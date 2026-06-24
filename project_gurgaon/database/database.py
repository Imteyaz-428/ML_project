from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL URL
DATABASE_URL = "mysql+pymysql://root:Password@host.docker.internal:3306/gurgaon_db"

# Create Engine
engine = create_engine(
    DATABASE_URL,
    echo=True
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
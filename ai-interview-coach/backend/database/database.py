import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {}}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

session = SessionLocal()

# ✅ Create Base FIRST
Base = declarative_base()

# ✅ Then import all models
from models.user import Users
from models.interview import Interview
from models.question import Question
from models.report import InterviewReport
from models.resume import Resume

# ✅ Finally create all tables
Base.metadata.create_all(bind=engine)
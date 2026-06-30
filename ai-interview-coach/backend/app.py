from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router as user_router
from routes.interview import router as interview_router
from routes.question import router as question_router
from routes.resume import router as resume_router
from routes.report import router as report_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-interview-coach-frontend-three.vercel.app",
        "https://ai-interview-coach-frontend-kov5h0p5b-imteyaz-428s-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(interview_router)
app.include_router(question_router)
app.include_router(resume_router)
app.include_router(report_router)

@app.get("/")
def home():
    return {"message": "AI Interview Coach API"}
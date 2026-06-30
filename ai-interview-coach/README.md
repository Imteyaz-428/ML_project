# 🚀 AI Interview Coach

AI Interview Coach is a full-stack web application that helps users prepare for technical interviews using Artificial Intelligence. The platform generates company-specific interview questions, evaluates user responses using AI, and provides detailed interview reports with personalized feedback and hiring recommendations.

---

# ✨ Features

## 👤 Authentication
- User Registration
- Secure Login using JWT Authentication
- User Profile Management

## 📄 Resume Analysis
- Upload Resume (PDF)
- AI-powered Resume Analysis
- Skill Extraction
- Resume Feedback

## 🎤 AI Mock Interview
- Company-specific Interview Questions
- Role-based Interview Questions
- Multiple Difficulty Levels
- AI Answer Evaluation
- Instant Feedback

## 📊 Interview Report
- Overall Interview Score
- Professional Summary
- Overall Performance Feedback
- Strong Technical Domains
- Weak Technical Domains
- Strengths
- Weaknesses
- Weak Skills
- Personalized Recommendations
- Hiring Decision

## 📁 Interview History
- View Previous Interviews
- Access Previous Reports
- Track Interview Performance

---

# 🛠 Tech Stack

## Frontend
- React.js
- React Router DOM
- Axios
- Vite

## Backend
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication

## Database
- MySQL

## AI Models
- Google Gemini
- Groq
- DeepSeek

---

# 📂 Project Structure

```text
AI-Interview-Coach
│
├── backend
│   ├── crud
│   ├── models
│   ├── routes
│   ├── schemas
│   ├── services
│   ├── prompts
│   ├── database
│   ├── utils
│   ├── config.py
│   └── app.py
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Imteyaz-428/AI-Interview-Coach.git

cd AI-Interview-Coach
```

---

# Backend Setup

```bash
cd backend
```

Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_KEY
GROQ_API_KEY=YOUR_GROQ_KEY
DEEPSEEK_API_KEY=YOUR_DEEPSEEK_KEY

SECRET_KEY=YOUR_SECRET_KEY

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=YOUR_PASSWORD
MYSQL_DATABASE=AIInterviewCoach
```

Run Backend

```bash
uvicorn app:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend
```

Install Packages

```bash
npm install
```

Run Frontend

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---



# 🚀 Future Improvements

- Voice-based AI Interview
- Coding Interview Support
- AI Follow-up Questions
- ATS Resume Score
- Company-specific Interview Sets
- Progress Analytics Dashboard
- Export Report as PDF
- Dark Mode

---

# 👨‍💻 Author

**Imteyaz Alam**

B.Tech – Artificial Intelligence & Machine Learning

Galgotias College of Engineering & Technology

GitHub:
https://github.com/Imteyaz-428

LinkedIn:
https://linkedin.com/in/imteyaz428

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
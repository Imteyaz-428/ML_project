# ML & Full-Stack AI Projects Collection

A collection of machine learning and full-stack AI applications built with Python, Scikit-learn, FastAPI, React, and Streamlit — spanning classical ML pipelines, LLM-powered systems, and end-to-end deployed platforms.

---

## Projects

### 1. [AI Interview Coach](./ai-interview-coach)
A full-stack AI mock-interview platform with resume analysis, role-specific question generation, and automated answer evaluation.

**Highlights**
- Multi-provider LLM architecture (Gemini, Groq, DeepSeek) with automatic fallback and retry logic
- Resume parsing and ATS scoring pipeline using PyMuPDF + LLM-based analysis
- JWT-authenticated FastAPI backend with MySQL/SQLAlchemy for users, interviews, and reports
- React (Vite) frontend with dynamic report visualization and PDF export

**Tech Stack:** FastAPI · React.js · MySQL · SQLAlchemy · JWT · Gemini · Groq · DeepSeek

**Links:** [GitHub](./ai-interview-coach) · [Live Demo](https://ai-interview-coach-frontend-three.vercel.app)

---

### 2. [Gurgaon House Price Prediction](./project_gurgaon)
An end-to-end ML platform predicting Gurgaon residential property prices, served via a REST API with authenticated prediction history.

**Highlights**
- Random Forest Regressor trained on log-transformed prices to handle target skew
- Custom scikit-learn transformer for locality/property-type frequency encoding
- Stratified sampling on price quantiles for a representative train/test split
- JWT-authenticated FastAPI backend with per-user prediction history in MySQL
- Containerized with Docker, deployed on Render with a cloud-hosted MySQL instance (Aiven)

**Tech Stack:** FastAPI · MySQL · SQLAlchemy · Scikit-learn · JWT · Docker

**Links:** [GitHub](./project_gurgaon) · [Live API](https://ml-project-glld.onrender.com/docs)

---

### 3. [Student Performance Predictor](./student_performance)
A Streamlit app predicting student academic performance from attendance, study habits, and prior grades.

**Highlights**
- End-to-end preprocessing pipeline (imputation, scaling, encoding) shared between training and inference
- Model comparison across Linear Regression, Decision Tree, and Random Forest via cross-validated RMSE
- Personalized improvement suggestions based on input risk factors

**Tech Stack:** Python · Pandas · NumPy · Scikit-learn · Streamlit

**Links:** [GitHub](./student_performance)

---

## Technologies Used

| Category | Tools |
|---|---|
| Languages | Python |
| Backend | FastAPI, REST APIs, SQLAlchemy, JWT Authentication |
| Machine Learning | Scikit-learn, Pandas, NumPy, Matplotlib, XGBoost |
| AI / LLM | Gemini, Groq, DeepSeek, PyMuPDF |
| Databases | MySQL, PostgreSQL |
| Frontend | React.js (Vite), Streamlit |
| DevOps | Docker, Git, GitHub, Render, Vercel, Aiven |

---

## Repository Structure

```text
ML_project/
│
├── ai-interview-coach/       # Full-stack AI mock-interview platform (FastAPI + React)
├── project_gurgaon/          # Gurgaon house price prediction API (FastAPI + Scikit-learn)
├── student_performance/      # Student performance predictor (Streamlit)
└── README.md
```

---

## Author

**Imteyaz Alam**
B.Tech, Artificial Intelligence and Machine Learning
Galgotias College of Engineering and Technology

[GitHub](https://github.com/Imteyaz-428) · [LinkedIn](https://linkedin.com/in/imteyaz428) · [LeetCode](https://leetcode.com/Imteyaz30)

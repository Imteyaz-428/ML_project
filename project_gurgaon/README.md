# 🏠 Gurgaon House Price Prediction System

A full-stack Machine Learning application that predicts residential property prices in Gurgaon based on various property features such as area, locality, BHK count, property type, RERA approval status, and rate per square foot.

The project combines Machine Learning, FastAPI, Frontend Development, and Docker to provide an end-to-end real estate price prediction solution.

---

## 🚀 Features

- Predict Gurgaon house prices using Machine Learning
- Custom Feature Engineering Pipeline
- FastAPI REST API
- Interactive Frontend Interface
- Dockerized Application
- Data Validation using Pydantic
- Automatic API Documentation with Swagger UI
- Scalable Project Structure

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- NumPy
- Pandas
- Scikit-Learn
- Joblib

### Backend
- FastAPI
- Pydantic
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Docker

---

## 📂 Project Structure

project_gurgaon/

├── auth/

├── crud/

├── data/

├── database/

├── fronted/

├── model/

│ ├── predict.py

│ └── model.pkl

├── schema/

├── utils/

├── app.py

├── feature_engineering.py

├── Dockerfile

├── requirements.txt

└── README.md

---

## 📊 Dataset Features

The model uses the following features:

| Feature | Description |
|----------|------------|
| Status | Ready to Move / Under Construction |
| Area | Property Area (sq ft) |
| Rate per sqft | Price per square foot |
| Property Type | Apartment, Villa, Plot, etc. |
| Locality | Gurgaon Sector/Location |
| RERA Approval | Approved / Not Approved |
| BHK Count | Number of Bedrooms |
| Flat Type | Apartment / Villa / Plot |

---

## 🔍 Feature Engineering

Custom Transformer:

```python
class RealEstateFeatureEngineer(BaseEstimator, TransformerMixin):
```

Generated Features:

- Property Type Frequency
- Locality Frequency
- Extracted BHK Value
- Main Property Category

Example Features:

```python
Property_Type_freq
Locality_freq
BHK
Main_Type
```

---

## 🤖 Machine Learning Pipeline

Pipeline Architecture:

```text
Feature Engineering
        ↓
Missing Value Imputation
        ↓
Scaling
        ↓
One Hot Encoding
        ↓
Random Forest Regressor
```

Model Used:

```python
RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
```

---

## 📡 API Endpoint

### Predict House Price

```http
POST /predict
```

### Sample Request

```json
{
  "Status": "Ready to Move",
  "Area": 920,
  "Rate_per_sqft": 4800,
  "Property_Type": "3 BHK Apartment",
  "Locality": "Sector 82",
  "RERA_Approval": "Not Approved by RERA",
  "BHK_Count": 3,
  "Flat_type": "Apartment"
}
```

### Sample Response

```json
{
  "predicted_price": 4382688.79
}
```

---

## 📖 API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Imteyaz-428/ML_project.git

cd ML_project/project_gurgaon
```

### Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

Start FastAPI Server:

```bash
uvicorn app:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t gurgaon-house-price .
```

### Run Docker Container

```bash
docker run -p 8000:8000 gurgaon-house-price
```

Open:

```text
http://localhost:8000/docs
```

---

## 📈 Future Improvements

- React Frontend
- Tailwind CSS UI
- User Authentication
- Prediction History
- Cloud Deployment
- Model Monitoring
- Price Trend Visualization
- Multiple Model Comparison

---

## 👨‍💻 Author

**Imteyaz Alam**

B.Tech (Artificial Intelligence & Machine Learning)

Galgotias College of Engineering & Technology

GitHub: https://github.com/Imteyaz-428

---

## ⭐ Resume Description

Developed a full-stack House Price Prediction System using Machine Learning, FastAPI, and Docker. Built a custom feature engineering pipeline, trained a Random Forest model, exposed predictions through REST APIs, and integrated a responsive frontend for real-time property price estimation in Gurgaon.
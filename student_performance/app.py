import streamlit as st
import pandas as pd
import joblib

# Load Model & Pipeline
model = joblib.load("model.pkl")
pipeline = joblib.load("pipeline.pkl")

st.title("🎓 Student Performance Predictor")

st.write("Enter student details below to predict Final Grade.")

# --- USER INPUT FIELDS ---

gender = st.selectbox("Gender", ["Male", "Female"])
attendance_rate = st.number_input("Attendance Rate (%)", min_value=0, max_value=100, value=75, step=1)
study_hours_per_week = st.number_input("Study Hours Per Week", min_value=0, max_value=50, value=0, step=1)
previous_grade = st.number_input("Previous Grade", min_value=0, max_value=100, value=0, step=1)
extracurricular = st.number_input("Extracurricular Activities (number)", min_value=0, max_value=10, value=0, step=1)
study_hours = st.number_input("Study Hours (daily)", min_value=0.0, max_value=10.0, value=0.0, format="%.0f")
attendance_percent = st.number_input("Attendance (%)", min_value=0, max_value=100, value=0, step=1)

parental_support = st.selectbox("Parental Support", ["Low", "Medium", "High"])
online_classes_taken = st.selectbox("Online Classes Taken?", ["True", "False"])

# Convert Boolean
online_classes_taken = True if online_classes_taken == "True" else False

# --- CREATE DF FOR MODEL ---
input_data = pd.DataFrame([{
    "Gender": gender,
    "AttendanceRate": attendance_rate,
    "StudyHoursPerWeek": study_hours_per_week,
    "PreviousGrade": previous_grade,
    "ExtracurricularActivities": extracurricular,
    "ParentalSupport": parental_support,
    "Study Hours": study_hours,
    "Attendance (%)": attendance_percent,
    "Online Classes Taken": online_classes_taken
}])

# --- PREDICT ---
if st.button("Predict Final Grade"):
    transformed = pipeline.transform(input_data)
    prediction = model.predict(transformed)
    st.success(f"📘 Predicted Final Grade: **{prediction[0]:.2f}**")
    if prediction < 50:
        category = "Low"
    elif prediction < 70:
        category = "Medium"
    elif prediction < 85:
        category = "Good"
    else:
        category = "Excellent"

    st.info(f"Performance Category: **{category}**")

st.sidebar.title("📚 Student Performance Predictor")
st.sidebar.write("Mini Project - BTech  AIML")
st.sidebar.write("Submitted by: Imteyaz alam")

st.bar_chart(input_data.T)

st.subheader("📉 Weak Areas & Improvement Suggestions")

weak_areas = []

# Check attendance
if attendance_rate < 70:
    weak_areas.append("Low Attendance: Try to maintain at least 75%–85% attendance.")

# Study hours per weekma
if study_hours_per_week < 10:
    weak_areas.append("Low Study Hours: Increase study time to at least 1–2 hours daily.")

# Daily study
if study_hours < 1:
    weak_areas.append("No Daily Study Habit: Study at least 45–60 minutes daily.")

# Previous grade
if previous_grade < 60:
    weak_areas.append("Weak Academic Base: Revise previous concepts and practice regularly.")

# Extracurricular
if extracurricular < 1:
    weak_areas.append("No Extracurricular Skills: Participate in activities to improve focus & discipline.")

# Parental Support
if parental_support == "Low":
    weak_areas.append("Low Support: Try discussing study challenges with faculty or mentor and also discuss with freinds.")

# Online classes
if not online_classes_taken:
    weak_areas.append("Not Attending Online Classes: Watch recorded lectures for revision.")


# Output
if weak_areas:
    for area in weak_areas:
        st.warning(area)
else:
    st.success("🎉 No major weak areas detected! Keep up the good work.")


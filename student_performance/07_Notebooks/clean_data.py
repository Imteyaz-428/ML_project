import numpy as np
import pandas as pd

data = pd.read_csv("student_performance_updated_1000.csv")
print(data.head())
data = data.copy()
# 01. remove negative study hours
median_value = data["Study Hours"].median() 
data.loc[data["Study Hours"] < 0, "Study Hours"] = median_value

#02 clean the attendance rate, if attedence is more than 100 then it replace to 100 and or attendent is less than 0 then it replace to 0
data.loc[:, "AttendanceRate"] = data["AttendanceRate"].clip(lower=0, upper=100)

#03  drop duplicate names
data = data.drop_duplicates(subset=["Name"])

data.to_csv("cleaned_student_data.csv", index =False)
data = data.dropna(subset=["FinalGrade"])
print(data.shape)


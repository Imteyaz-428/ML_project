# This script compares multiple regression models
# (Linear Regression, Decision Tree, Random Forest)
# using RMSE to select the best-performing model.

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 1. Load & clean data

data = pd.read_csv("cleaned_student_data.csv")

data = data.dropna(subset=["FinalGrade"])
data = data[(data["FinalGrade"] >= 0) & (data["FinalGrade"] <= 100)]
data = data.reset_index(drop=True)


# 2. Stratified Splitting

data["grade"] = pd.cut(
    data["FinalGrade"],
    bins=[0, 50, 70, 85, np.inf],
    labels=["low", "upperlow", "mid", "high"]
)

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_idx, test_idx in split.split(data, data["grade"]):
    train_set = data.loc[train_idx].drop("grade", axis=1)
    test_set = data.loc[test_idx].drop("grade", axis=1)

# Use only training set for choosing best model
student_labels = train_set["FinalGrade"]
student_features = train_set.drop("FinalGrade", axis=1)

# Remove non-useful columns
cols_to_remove = ["StudentID", "Name"]
for col in cols_to_remove:
    if col in student_features.columns:
        student_features = student_features.drop(col, axis=1)

# Identify numerical & categorical columns
num_attribs = student_features.select_dtypes(include=[np.number]).columns.tolist()
cat_attribs = student_features.select_dtypes(exclude=[np.number]).columns.tolist()




# 3. Build preprocessing pipeline

num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs)
])

# Transform data
student_prepared = full_pipeline.fit_transform(student_features)




# 4. Train and Compare Models

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42)
}

model_scores = {}

print("\n🔹 Evaluating Models (Using RMSE)...")

for name, model in models.items():
    scores = -cross_val_score(
        model,
        student_prepared,
        student_labels,
        scoring="neg_root_mean_squared_error",
        cv=10
    )
    rmse = scores.mean()
    model_scores[name] = rmse
    print(f"{name} -> RMSE = {rmse}")



# 5. Print Best Model

best_model_name = min(model_scores, key=model_scores.get)
best_rmse = model_scores[best_model_name]

print(f" BEST MODEL: {best_model_name}")
print(f"RMSE: {best_rmse}")


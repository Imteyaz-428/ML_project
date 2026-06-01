import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score


MODEL_FILE = "model.pkl"
PIPELINE_FILE = 'pipeline.pkl'

def build_pipeline(num_attribute, cat_attribute) :
    #for numberical columns
    num_pipeline = Pipeline([
    ("imputer" , SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    #for categorical columns
    cat_pipeline = Pipeline([
        ("onehot",OneHotEncoder(handle_unknown="ignore"))
    ])


    #  consturct the full pipeline
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribute),
        ("cat", cat_pipeline, cat_attribute)
    ])
    return full_pipeline

if not os.path.exists(MODEL_FILE):
    #lets train the model
    # 01. Load the dataset
    data = pd.read_csv("cleaned_student_data.csv")
    data = data.dropna(subset=["FinalGrade"])     # remove NaN grades
    data = data[data["FinalGrade"] >= 0]          # remove invalid negatives
    data = data[data["FinalGrade"] <= 100]        # remove unrealistic >100
    
    
    data = data.reset_index(drop=True)
    
    # 02 . create a stratified test test
    data["grade"] = pd.cut(data["FinalGrade"], bins =[0, 50,70,85,np.inf], labels = ["low", "upperlow", "mid","high"])
    split = StratifiedShuffleSplit(n_splits=1,test_size=0.2, random_state=42)

    for train_index, test_index in split.split(data, data["grade"]):
        
        data.loc[test_index].drop("grade", axis =1).to_csv("input.csv", index=False)
        data = data.loc[train_index].drop("grade", axis =1)
       
    
    student_labels = data["FinalGrade"].copy()
    student_features = data.drop("FinalGrade", axis =1)
    
    # Remove unwanted columns before feature selection
    cols_to_remove = ["StudentID", "Name"]

    for col in cols_to_remove:
        if col in student_features.columns:
            student_features = student_features.drop(col, axis=1)

    # Now recalculate features
    num_attribute = student_features.select_dtypes(include=[np.number]).columns.tolist()
    cat_attribute = student_features.select_dtypes(exclude=[np.number]).columns.tolist()

    pipeline = build_pipeline(num_attribute, cat_attribute)
   
    student_prepared =pipeline.fit_transform(student_features)
    model = LinearRegression()
    model.fit(student_prepared, student_labels)
    
    joblib.dump(model, MODEL_FILE)
    joblib.dump(pipeline,PIPELINE_FILE)
    
    
    print("model is trained. CONGRATS!")
    
    # print(student_prepared)

else :   
    # INFERENCE PHASE
    model = joblib.load(MODEL_FILE)
    pipeline = joblib.load(PIPELINE_FILE)
 
    input_data = pd.read_csv("input.csv")
    transformed_input = pipeline.transform(input_data)
    predictions = model.predict(transformed_input)
    input_data["FinalGrade"] = predictions
 
    input_data.to_csv("output.csv", index=False)
    print("Inference complete. Results saved to output.csv")
    
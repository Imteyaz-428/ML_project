import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from utils.feature_engineering import RealEstateFeatureEngineer

MODEL_FILE = "model/model.pkl"
PIPELINE_FILE = "pipleline.pkl"


    

def build_pipeline(num_attribute, cat_attribute) :
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    
    
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])
    
    
    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, num_attribute),
        ("cat", categorical_pipeline, cat_attribute)
        
    ])
    
    
    full_pipeline = Pipeline([
        ("feature_engineering", RealEstateFeatureEngineer()),
        ("preprocessing", preprocessor),
        
        ("model", RandomForestRegressor(
            n_estimators=200,
            random_state=42
        ))
    ])
    return full_pipeline 


if not os.path.exists(MODEL_FILE):
    # TRAINING PHASE
    
    #1 load the data 
    df = pd.read_csv("data/data of gurugram real Estate.csv")

    # 2 data cleaning step
    df["Price"] = df["Price"].str.replace(",", "")
    df["Price"] = df["Price"].astype(float) # changing price type object to float
    df = df.drop(["Builder Name", "Company Name"], axis=1) # drop unnaccessary features
    df["Rate per sqft"] = df["Rate per sqft"].str.replace(",", "")  # change rate per sqft ot int
    df["Rate per sqft"] = df["Rate per sqft"].astype(int)
    df.drop("Socity", axis=1, inplace=True) # drop socity because it is unnaccessary feature
    df = df[df["Area"] < 10000] # clean data from outliers
    df = df[df["BHK_Count"] >= 1] # clean bhk count
    df["BHK_Count"] = df["BHK_Count"].astype(int) # change bhk type from oject to int
    df = df[df["BHK_Count"] <= 10]
    df["Log_Price"] = np.log1p(df["Price"]) # taking log price because price is heavily right skewed


    # 3 create a stratified suffle and split
    df["price_bin"] = pd.qcut(
        df["Log_Price"],
        q=5,
        labels=False
    )
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

    for train_index, test_index in split.split(df, df["price_bin"]):
        strat_train_set = df.iloc[train_index].copy()
        strat_test_set = df.iloc[test_index].copy()
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("price_bin", axis=1, inplace=True)
        
    feature_train = strat_train_set.drop(["Price", "Log_Price"],axis=1)
    labels_train = strat_train_set["Log_Price"]
    
    # Save test set separately if you want
    strat_test_set.to_csv("data/input.csv", index=False)
   
   
    numeric_features = [
        "Area", "BHK_Count", "Rate per sqft",
        "Property_Type_freq", "Locality_freq", "BHK"
    ]


   
    categorical_features = [
        "Main_Type",
        "Status",
        "RERA Approval",
        "Flat Type"
    ]
    model = build_pipeline(numeric_features, categorical_features)
    model.fit(feature_train, labels_train)
    
    
    joblib.dump(model, MODEL_FILE)

    print("Model saved successfully.")
    
else :
     # INFERENCE PHASE
    model = joblib.load(MODEL_FILE)
    
    
    input_data = pd.read_csv("data/input.csv")
    
    pred_log = model.predict(input_data)
    pred_price = np.expm1(pred_log)
    input_data["predicted_price"] = pred_price
    input_data.to_csv("data/output.csv", index=False)
    print("Inference complete. Results saved to output.csv")
    
    
    

    
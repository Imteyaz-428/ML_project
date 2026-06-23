from schema.user_input import UserInput
import joblib

from utils.feature_engineering import RealEstateFeatureEngineer
from fastapi.middleware.cors import CORSMiddleware

with open('model/model.pkl', 'br') as f :
    model = joblib.load(f)


MODLE_VERSION = 1.0
from utils.feature_engineering import RealEstateFeatureEngineer
import joblib
import pandas as pd
import numpy as np

def predict_output(data) :
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    actual_price = np.expm1(prediction[0])
    return int(actual_price)
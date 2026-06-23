from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import MODLE_VERSION, predict_output, model
import pandas as pd;
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


  
@app.get('/') 
def home() :
    return {"Home page" : "House price prediction of gurgaon city"}


@app.get('/price') 
def price_prediction() :
    return {
        'status' : 'ok',
        'version' : MODLE_VERSION
    }
    
@app.post('/predict') 
def predict(house_info : UserInput) :
    data = {

        "Status": house_info.Status,
        "Area": house_info.Area,
        "Rate per sqft": house_info.Rate_per_sqft,
        "Property Type": house_info.Property_Type,
        "Locality": house_info.Locality,
        "RERA Approval": house_info.RERA_Approval,
        "BHK_Count": house_info.BHK_Count,
        "Flat Type" : house_info.Flat_type
    }
    actual_price = predict_output(data)
    return JSONResponse(status_code=200, content={"predicted price " : actual_price})
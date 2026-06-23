from fastapi import FastAPI , Depends, HTTPException
from sqlalchemy.orm import Session
from model.prediction import Prediction
from database.database import get_db
from fastapi.responses import JSONResponse
from schema.user_input import UserInput 
from schema.user import UserCreate, UserResponse
from utils.jwt_handler import create_access_token
from utils.auth import get_current_user

from crud.crud import create_user, get_user_by_email
from model.predict import MODLE_VERSION, predict_output, model
from schema.login import LoginRequest
from utils.hash import verify_password
import pandas as pd;
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
from database.database import engine, Base

from model.user import Users

Base.metadata.create_all(bind=engine)

from model.prediction import Prediction
Base.metadata.create_all(bind=engine)


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
    
from fastapi import Depends
from sqlalchemy.orm import Session

@app.post('/predict')
def predict(
    house_info: UserInput,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    data = {
        "Status": house_info.Status,
        "Area": house_info.Area,
        "Rate per sqft": house_info.Rate_per_sqft,
        "Property Type": house_info.Property_Type,
        "Locality": house_info.Locality,
        "RERA Approval": house_info.RERA_Approval,
        "BHK_Count": house_info.BHK_Count,
        "Flat Type": house_info.Flat_type
    }

    actual_price = predict_output(data)

    user = get_user_by_email(
        db,
        current_user
    )

    prediction = Prediction(
        user_id=user.id,
        locality=house_info.Locality,
        bhk=house_info.BHK_Count,
        area=house_info.Area,
        predicted_price=float(actual_price)
    )

    db.add(prediction)
    db.commit()

    return JSONResponse(
        status_code=200,
        content={"predicted price": actual_price}
    )
@app.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = create_user(
        db,
        user
    )

    return new_user

@app.post("/login")
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):

    db_user = get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    token = create_access_token(
    {
        "sub": db_user.email
    }
)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    
@app.get("/profile")
def profile(
    current_user: str = Depends(get_current_user)
):
    return {
        "email": current_user
    }
    
    
@app.get("/history")
def history(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = get_user_by_email(
        db,
        current_user
    )

    predictions = (
        db.query(Prediction)
        .filter(Prediction.user_id == user.id)
        .all()
    )

    return predictions
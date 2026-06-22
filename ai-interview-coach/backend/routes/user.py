from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field, EmailStr,field_validator
from typing import Annotated
import json
import re
from schemas.user import User, User_update

from crud.user import create_user, update_user, delete_user, get_user




router = APIRouter()

# class User(BaseModel) :
#     name: Annotated[str,Field(..., description="name of the user")]
#     email: Annotated[EmailStr, Field(...,description="email of the user")] 
#     password : str
#     @field_validator("password")
#     @classmethod
#     def validate_password(cls, value):
#         if len(value) < 8:
#             raise ValueError("Password must be at least 8 characters")
#         if not re.search(r"[a-z]", value):
#             raise ValueError("Password must contain a lowercase letter")
#         if not re.search(r"[A-Z]", value):
#             raise ValueError("Password must contain an uppercase letter")
#         if not re.search(r"\d", value):
#             raise ValueError("Password must contain a digit")
#         if not re.search(r"[@$!%*?&]", value):
#             raise ValueError("Password must contain a special character")
#         return value
    
    
    
# def load_user_data() :
#     with open("user_data.json", "r") as f:
#         data = json.load(f)
#     return data


# def save_user_data(data) :
#     with open("user_data.json", "w") as f:
#         json.dump(data,f)
        


# @router.get("/users")
# def get_users():
#     data = load_user_data()
#     return [{"message": "All Users"},data]




# @router.get("/single_user_data")
# def user_in_db(
#     gmail: str = Query(..., description="Check whether email exists")
# ):
#     data = load_user_data()
#     if(gmail in data) :
#         return data[gmail]
    
#     raise HTTPException(status_code=400,detail="user not exist in database")
    

# @router.post("/create") 
# def add_users(user:User):
#     # load previous data
#     data = load_user_data()
    
    
#     # check if user already registered
#     if(user.email in data) :
#         raise HTTPException(status_code=400,detail="user already exist in database")
    
#     # add the data in database
#     data[user.email] = user.model_dump()
    
#     # again reform to json
#     save_user_data(data)
    
    
#     # return response
#     return JSONResponse(status_code=201,content={"message": "user data added successfully"})

@router.post('/create', response_model=User) 
def add_user(user : User) :
    return create_user(user)

@router.get('/get') 
def get_users(Email: EmailStr) :
    return get_user(Email)

@router.put('/update') 
def update_users(Email: EmailStr, user: User_update) :
    return update_user(Email, user)

@router.delete('/delete')
def delete_users(Email: EmailStr) :
    return delete_user(Email)
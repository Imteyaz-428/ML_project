from fastapi import APIRouter, Query
from pydantic import Field, EmailStr,field_validator
from schemas.user import User, User_update,UserResponse
from fastapi import Depends
from utils.oauth2 import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

from crud.user import create_user, update_user, delete_user, get_user,login




router = APIRouter()

@router.post('/Register', response_model=User) 
def add_user(user : User) :
    return create_user(user)

@router.get("/Profile", response_model=UserResponse)
def profile(current_user=Depends(get_current_user)):
    return current_user

@router.put('/update') 
def update_users(Email: EmailStr, user: User_update) :
    return update_user(Email, user)

@router.delete('/delete')
def delete_users(Email: EmailStr) :
    return delete_user(Email)

@router.post('/login') 
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):

    email = form_data.username

    password = form_data.password
    return login(email, password)
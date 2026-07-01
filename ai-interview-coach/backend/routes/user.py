from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from schemas.user import User, User_update, UserResponse
from utils.oauth2 import get_current_user
from database.database import get_db
from crud.user import create_user, update_user, delete_user, get_user, login

router = APIRouter()


@router.post('/Register', response_model=User)
def add_user(user: User, db: Session = Depends(get_db)):
    return create_user(user, db)


@router.get("/Profile", response_model=UserResponse)
def profile(current_user=Depends(get_current_user)):
    return current_user


@router.put('/update')
def update_users(Email: EmailStr, user: User_update, db: Session = Depends(get_db)):
    return update_user(Email, user, db)


@router.delete('/delete')
def delete_users(Email: EmailStr, db: Session = Depends(get_db)):
    return delete_user(Email, db)


@router.post('/login')
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login(form_data.username, form_data.password, db)

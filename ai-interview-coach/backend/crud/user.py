from fastapi import HTTPException
from database.database import engine, session
from pydantic import EmailStr
from schemas.user import User, User_update
from models.user import Users
from sqlalchemy.exc import IntegrityError
from utils.security import hash_password, verify_password
from utils.jwt import create_access_token

def create_user(user_data : User) :
    try:
        user = Users(
            Email = user_data.Email,
            Name = user_data.Name,
            Age = user_data.Age,
            Gender = user_data.Gender,
            Trade = user_data.Trade,
            password=hash_password(user_data.password)  
        )
        
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=404,
            detail='user email already exist'
        )
    

def update_user(email: EmailStr,user_data : User_update) :
    db_user = session.query(Users).filter_by(Email = email).first()
    if not db_user :
    
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )
    
    update_data = user_data.model_dump(exclude_unset=True)

    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])

    for key, value in update_data.items():
        setattr(db_user, key, value)
        
    session.commit()
    session.refresh(db_user)
    return db_user
        

def get_user(Email :EmailStr) :
    db_user = session.query(Users).filter_by(Email = Email).first()
    if not db_user :

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return db_user

def delete_user(Email : EmailStr) :
    db_user = session.query(Users).filter_by(Email = Email).first()
    if not db_user :
        
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    session.delete(db_user)
    session.commit()
    
    return {"message " :"user data deleted succussfully"}

def login(Email: EmailStr, password: str):
    db_user = session.query(Users).filter_by(Email=Email).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="Please enter correct email"
        )

    if not verify_password(password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid Email or password"
        )
    

    token = create_access_token(
        {"sub": db_user.Email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    
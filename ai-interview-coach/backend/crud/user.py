from fastapi import HTTPException
from database.database import engine, session
from pydantic import EmailStr
from schemas.user import User, User_update
from models.user import Users
from sqlalchemy.exc import IntegrityError


def create_user(user_data : User) :
    try:
        user = Users(
            Email = user_data.Email,
            Name = user_data.Name,
            Age = user_data.Age,
            Gender = user_data.Gender,
            Trade = user_data.Trade,
            password = user_data.password   
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

def login(Email :EmailStr, password:str) :
    db_user = session.query(Users).filter_by(Email=Email).first()
    if not db_user :
        raise HTTPException(
            status_code=404,
            detail="please put correct email"
        )
        
    if(db_user.password != password) :
        raise HTTPException(
            status_code=404,
            detail="please enter correct password"
        )
        
    return db_user
    
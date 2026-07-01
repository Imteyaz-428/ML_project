from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from schemas.user    import User, User_update
from models.user     import Users
from utils.security  import hash_password, verify_password
from utils.jwt       import create_access_token


def create_user(user_data: User, db: Session):
    try:
        user = Users(
            Email    = user_data.Email,
            Name     = user_data.Name,
            Age      = user_data.Age,
            Gender   = user_data.Gender,
            Trade    = user_data.Trade,
            password = hash_password(user_data.password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError:
        db.rollback()
        # ✅ FIX 7: Changed status_code from 404 → 409 (Conflict)
        # 404 means "Not Found" which is wrong for a duplicate email scenario.
        # 409 Conflict is the correct HTTP status for "resource already exists".
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )


def update_user(email: EmailStr, user_data: User_update, db: Session):
    db_user = db.query(Users).filter_by(Email=email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_data.model_dump(exclude_unset=True)

    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(Email: EmailStr, db: Session):
    db_user = db.query(Users).filter_by(Email=Email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


def delete_user(Email: EmailStr, db: Session):
    db_user = db.query(Users).filter_by(Email=Email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


def login(Email: EmailStr, password: str, db: Session):
    db_user = db.query(Users).filter_by(Email=Email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="Please enter correct email")

    if not verify_password(password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid Email or password")

    token = create_access_token({"sub": db_user.Email})
    return {"access_token": token, "token_type": "bearer"}

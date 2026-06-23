from sqlalchemy.orm import Session
from model.user import Users
from schema.user import UserCreate
from auth.hashing import hash_password


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(Users)
        .filter(Users.email == email)
        .first()
    )


def create_user(
    db: Session,
    user: UserCreate
):
    
    hashed_password = hash_password(
        user.password
    )

    new_user = Users(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

from model.user import Users

def get_user_by_email(
    db,
    email: str
):
    return (
        db.query(Users)
        .filter(Users.email == email)
        .first()
    )
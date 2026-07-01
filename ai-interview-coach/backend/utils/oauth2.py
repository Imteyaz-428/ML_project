from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from utils.jwt import verify_access_token
from database.database import get_db
from models.user import Users

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    email   = verify_access_token(token)
    db_user = db.query(Users).filter_by(Email=email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

from utils.jwt import verify_access_token
from database.database import session
from models.user import Users

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
def get_current_user(token: str = Depends(oauth2_scheme)):
    email = verify_access_token(token)
    db_user = session.query(Users).filter_by(Email=email).first()
    if not db_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return db_user


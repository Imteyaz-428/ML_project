from jose import jwt, JWTError
from fastapi import HTTPException
from datetime import datetime, timedelta

SECRET_KEY = "your_super_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 300


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

from jose import jwt, JWTError

def verify_access_token(token: str):

    print("Received Token:", token)

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("Payload:", payload)

        email = payload.get("sub")

        print("Email:", email)

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return email

    except JWTError as e:

        print("JWT ERROR:", e)

        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )
from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class UserCreate(BaseModel):
    email: EmailStr

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="User Name"
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=25,
        description="Strong Password"
    )

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):

        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[@$!%*?&])"
            r"[A-Za-z\d@$!%*?&]{8,25}$"
        )

        if not re.match(pattern, value):
            raise ValueError(
                "Password must contain at least one uppercase letter, "
                "one lowercase letter, one digit, and one special character."
            )

        return value


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str

    model_config = {
        "from_attributes": True
    }
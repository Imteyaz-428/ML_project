from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated,Literal,Optional
import json
 
class User(BaseModel) :
    Email : EmailStr
    Name : Annotated[str, Field(..., description='name of the user', examples=["imteyaz alam"])]
    Age : Annotated[int, Field(..., gt=0,lt=150,description='age of the user')]
    Gender : Literal['male','female','other']
    Trade: Annotated[str,Field(..., description="field of the user", examples=["computer science"])]
    password : Annotated[str,Field(..., description="password of the user")]
    
    
class User_update(BaseModel) :
    Email : EmailStr
    Name : Annotated[Optional[str], Field(default=None)]
    Age : Annotated[Optional[int], Field(default=None,gt=0,l=150)]
    Gender : Optional[Literal['male', 'female', 'other']]= None
    Trade : Annotated[Optional[str], Field(default=None)]
    password : Annotated[Optional[str], Field(default=None)]
    
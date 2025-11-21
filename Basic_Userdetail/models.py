from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    Male = 'male'
    Female = 'female'

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: Gender
    mobile_no: int
    
class UpdateUser(BaseModel):
    name : Optional[str|None] = None
    email : Optional[EmailStr|None] = None
    gender : Optional[Gender|None] = None
    mobile_no : Optional[int|None] = None
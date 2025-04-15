from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
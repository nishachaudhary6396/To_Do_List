from pydantic import BaseModel, EmailStr
from typing import Optional


# User Registration Schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# User Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Create Task Schema
class TaskCreate(BaseModel):
    title: str
    description: str


# Update Task Schema
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


# for login
class UserLogin(BaseModel):
    username: str
    password: str
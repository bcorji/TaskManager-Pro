from pydantic import BaseModel, EmailStr, conint
from typing import Optional, List
from datetime import datetime
from .models.user import UserRole

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: UserRole
    is_active: bool

    class Config:
        orm_mode = True

# Task schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: conint(ge=1, le=3) = 1  # 1: Low, 2: Medium, 3: High

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: Optional[bool] = None

class Task(TaskBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[UserRole] = None
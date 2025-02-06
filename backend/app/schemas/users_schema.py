from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = None
    profile_picture: Optional[str] = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    password: Optional[str] = Field(None, min_length=6)


class UserOut(UserBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

    @staticmethod
    def from_orm_with_iso_dates(user):
        if not hasattr(user, "__table__"):
            user = dict(user)

        user["created_at"] = (
            user["created_at"].isoformat() if user["created_at"] else None
        )
        user["updated_at"] = (
            user["updated_at"].isoformat() if user["updated_at"] else None
        )

        return UserOut(**user)

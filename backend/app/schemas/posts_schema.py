from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    user_id: int
    category_id: Optional[int] = None
    title: str
    slug: str
    content: str
    featured_image: Optional[str] = None
    is_published: Optional[bool] = False
    youtube_video_url: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None
    featured_image: Optional[str] = None
    is_published: Optional[bool] = None
    youtube_video_url: Optional[str] = None
    category_id: Optional[int] = None


class PostOut(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CommentBase(BaseModel):
    post_id: int
    user_id: Optional[int] = None
    content: str
    parent_comment_id: Optional[int] = None


class CommentCreate(CommentBase):
    pass


class CommentUpdate(BaseModel):
    content: str


class CommentOut(CommentBase):
    id: int
    created_at: datetime
    updated_at: datetime

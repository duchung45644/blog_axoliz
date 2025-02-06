from pydantic import BaseModel


class PostTagBase(BaseModel):
    post_id: int
    tag_id: int


class PostTagCreate(PostTagBase):
    pass


class PostTagOut(PostTagBase):
    pass

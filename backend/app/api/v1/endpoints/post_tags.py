from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post_tags_schema import PostTagCreate, PostTagOut
from app.crud.post_tags_crud import (
    create_post_tag,
    get_post_tags,
    get_posts_by_tag,
    delete_post_tag,
)
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=dict)
def create_post_tag_endpoint(post_tag: PostTagCreate, db: Session = Depends(get_db)):
    return create_post_tag(db, post_tag)


@router.get("/post/{post_id}", response_model=list[PostTagOut])
def get_post_tags_endpoint(post_id: int, db: Session = Depends(get_db)):
    return get_post_tags(db, post_id)


@router.get("/tag/{tag_id}", response_model=list[PostTagOut])
def get_posts_by_tag_endpoint(tag_id: int, db: Session = Depends(get_db)):
    return get_posts_by_tag(db, tag_id)


@router.delete("/{post_id}/{tag_id}")
def delete_post_tag_endpoint(post_id: int, tag_id: int, db: Session = Depends(get_db)):
    return delete_post_tag(db, post_id, tag_id)

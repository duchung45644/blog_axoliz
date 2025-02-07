from fastapi import APIRouter, Depends, Query
from typing import Optional, List
from sqlalchemy.orm import Session
from app.schemas.posts_schema import PostCreate, PostUpdate, PostOut
from app.crud.posts_crud import (
    create_post,
    get_all_posts,
    get_post_by_id,
    search_posts,
    update_post,
    delete_post,
)
from app.database import get_db


router = APIRouter()


@router.post("/", response_model=dict)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)


@router.get("/", response_model=List[PostOut])
def get_posts_endpoint(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    search: Optional[str] = None,
    category_id: Optional[int] = None,
    is_published: Optional[bool] = None,
):
    return get_all_posts(
        db,
        limit=limit,
        offset=offset,
        search=search,
        category_id=category_id,
        is_published=is_published,
    )


@router.get("/search", response_model=List[PostOut])
def search_posts_endpoint(
    query: str = Query(..., min_length=1),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return search_posts(db, query, limit, offset)


@router.get("/{post_id}", response_model=PostOut)
def get_post_by_id_endpoint(post_id: int, db: Session = Depends(get_db)):
    return get_post_by_id(db, post_id)


@router.put("/{post_id}")
def update_post_endpoint(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    return update_post(db, post_id, post)


@router.delete("/{post_id}")
def delete_post_endpoint(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)

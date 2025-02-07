from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.comments_schema import CommentCreate, CommentUpdate, CommentOut
from app.crud.comments_crud import (
    create_comment,
    get_comments_by_post,
    get_comment_by_id,
    update_comment,
    delete_comment,
)
from app.database import get_db
from app.middleware.login import get_current_user

router = APIRouter()


@router.post("/", response_model=dict)
def create_comment_endpoint(
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return create_comment(db, comment)


@router.get("/post/{post_id}", response_model=list[CommentOut])
def get_comments_by_post_endpoint(post_id: int, db: Session = Depends(get_db)):
    return get_comments_by_post(db, post_id)


@router.get("/{comment_id}", response_model=CommentOut)
def get_comment_by_id_endpoint(comment_id: int, db: Session = Depends(get_db)):
    return get_comment_by_id(db, comment_id)


@router.put("/{comment_id}")
def update_comment_endpoint(
    comment_id: int,
    comment: CommentUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return update_comment(db, comment_id, comment)


@router.delete("/{comment_id}")
def delete_comment_endpoint(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return delete_comment(db, comment_id)

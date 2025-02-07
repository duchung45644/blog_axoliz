from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.tags_schema import TagCreate, TagUpdate, TagOut
from app.crud.tags_crud import (
    create_tag,
    get_tags,
    get_tag_by_id,
    update_tag,
    delete_tag,
)
from app.database import get_db
from app.middleware.login import get_current_user

router = APIRouter()


@router.post("/", response_model=TagOut)
def create_tag_endpoint(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)


@router.get("/", response_model=list[TagOut])
def get_tags_endpoint(db: Session = Depends(get_db)):
    return get_tags(db)


@router.get("/{tag_id}", response_model=TagOut)
def get_tag_by_id_endpoint(
    tag_id: int,
    db: Session = Depends(get_db),
):
    return get_tag_by_id(db, tag_id)


@router.put("/{tag_id}", response_model=TagOut)
def update_tag_endpoint(
    tag_id: int,
    tag: TagUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return update_tag(db, tag_id, tag)


@router.delete("/{tag_id}")
def delete_tag_endpoint(
    tag_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return delete_tag(db, tag_id)

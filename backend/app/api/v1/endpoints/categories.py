from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.categories_schema import CategoryCreate, CategoryUpdate, CategoryOut
from app.crud.categories_crud import (
    create_category,
    get_categories,
    get_category_by_id,
    update_category,
    delete_category,
)
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=dict)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)


@router.get("/", response_model=list[CategoryOut])
def get_categories_endpoint(db: Session = Depends(get_db)):
    return get_categories(db)


@router.get("/{category_id}", response_model=CategoryOut)
def get_category_by_id_endpoint(category_id: int, db: Session = Depends(get_db)):
    return get_category_by_id(db, category_id)


@router.put("/{category_id}")
def update_category_endpoint(
    category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)
):
    return update_category(db, category_id, category)


@router.delete("/{category_id}")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)

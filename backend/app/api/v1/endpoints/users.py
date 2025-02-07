from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

from app.crud.users_crud import create_user, delete_user, get_user, update_user
from app.schemas.users_schema import UserCreate, UserOut, UserUpdate
from app.middleware.login import get_current_user


router = APIRouter()


@router.post("/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    response = create_user(db, user)
    new_user_id = response["user_id"]
    user_data = get_user(db, new_user_id)
    return UserOut.from_orm_with_iso_dates(user_data)


@router.get("/{user_id}", response_model=UserOut)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user_data = get_user(db, user_id)
    return UserOut.from_orm_with_iso_dates(user_data)


@router.put("/{user_id}", response_model=UserOut)
def update_user_endpoint(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    update_user(db, user_id, user)
    updated_user = get_user(db, user_id)
    return UserOut.from_orm_with_iso_dates(updated_user)


@router.delete("/{user_id}")
def delete_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    try:
        get_user(db, user_id)
        delete_user(db, user_id)
        return {"message": "User deleted successfully"}
    except HTTPException:
        raise HTTPException(status_code=404, detail="User not found")

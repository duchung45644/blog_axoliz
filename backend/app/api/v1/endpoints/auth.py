from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.database import get_db
from app.schemas.login_schema import LoginSchema, Token
from app.utils.auth import create_access_token, verify_password
from app.crud.auth_crud import authenticate_user
from datetime import timedelta
from app.config.base import settings

router = APIRouter()


@router.post("/login", response_model=Token)
def login(user_credentials: LoginSchema, db: Session = Depends(get_db)):
    user_id = authenticate_user(
        db, user_credentials.username, user_credentials.password
    )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user_id)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db
from app.schemas.login_schema import LoginSchema, Token
from app.utils.auth import create_access_token
from datetime import timedelta
from config.base import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/login", response_model=Token)
def login(user_credentials: LoginSchema, db: Session = Depends(get_db)):
    try:
        result = db.execute(
            text("SELECT func_users_authenticate(:username, :password)"),
            {
                "username": user_credentials.username,
                "password": user_credentials.password,
            },
        ).fetchone()

        if not result or result[0] is None:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        user_id = result[0]
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user_id)}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

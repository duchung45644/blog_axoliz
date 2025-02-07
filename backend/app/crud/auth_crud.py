from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException
import psycopg2

from app.constants import ErrorMessages as ErrMsg


def authenticate_user(db: Session, username: str, password: str):
    try:
        result = db.execute(
            text("SELECT func_users_authenticate(:username, :password)"),
            {"username": username, "password": password},
        ).fetchone()

        if not result or result[0] is None:
            raise HTTPException(status_code=401, detail=ErrMsg.INVALID_CREDENTIALS)

        return result[0]

    except Exception as e:
        if "Invalid username or password" in str(e):
            raise HTTPException(status_code=401, detail=ErrMsg.INVALID_CREDENTIALS)
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

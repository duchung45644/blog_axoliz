from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.utils.auth import decode_access_token
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload["sub"]
    user = db.execute(
        text("SELECT * FROM users WHERE id = :user_id"), {"user_id": user_id}
    ).fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

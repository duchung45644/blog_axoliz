from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def authenticate_user(db: Session, username: str, password: str):
    result = db.execute(
        text("SELECT func_users_authenticate(:username, :password)"),
        {"username": username, "password": password},
    ).fetchone()

    return result[0] if result else None

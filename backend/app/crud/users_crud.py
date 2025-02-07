from sqlalchemy.sql import text
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.constants import ErrorMessages as ErrMsg
from app.schemas.users_schema import UserCreate, UserUpdate
from app.models.users import User


def create_user(db: Session, user: UserCreate):
    try:
        result = db.execute(
            text(
                """
                SELECT func_users_create(
                    :username,
                    :email,
                    :password,
                    :full_name,
                    :profile_picture,
                    :bio
                )
            """
            ),
            {
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "full_name": user.full_name,
                "profile_picture": user.profile_picture,
                "bio": user.bio,
            },
        ).fetchone()

        db.commit()
        return {"message": "User created successfully", "user_id": result[0]}

    except Exception as e:
        error_message = str(e)

        if "username-exists" in error_message:
            raise HTTPException(status_code=400, detail=ErrMsg.USERNAME_EXISTS)
        elif "email-exists" in error_message:
            raise HTTPException(status_code=400, detail=ErrMsg.EMAIL_EXISTS)

        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )


def update_user(db: Session, user_id: int, user: UserUpdate):
    db.execute(
        text(
            """
            SELECT func_users_update(
                :id, 
                :full_name, 
                :profile_picture, 
                :bio, 
                :password
            )
        """
        ),
        {
            "id": user_id,
            "full_name": user.full_name,
            "profile_picture": user.profile_picture,
            "bio": user.bio,
            "password": user.password if user.password else None,
        },
    )
    db.commit()
    return {"message": "User updated successfully"}


def delete_user(db: Session, user_id: int):
    result = db.execute(text("CALL func_users_delete(:id)"), {"id": user_id})

    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail=ErrMsg.USER_NOT_FOUND)

    return {"message": "User deleted successfully"}


def get_user(db: Session, user_id: int):
    result = (
        db.execute(text("SELECT * FROM func_users_read(:id)"), {"id": user_id})
        .mappings()
        .fetchone()
    )

    if not result:
        raise HTTPException(status_code=404, detail=ErrMsg.USER_NOT_FOUND)

    return result

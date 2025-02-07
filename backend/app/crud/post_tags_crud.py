from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException

from app.constants import ErrorMessages as ErrMsg
from app.schemas.post_tags_schema import PostTagCreate


def create_post_tag(db: Session, post_tag: PostTagCreate):
    result = db.execute(
        text(
            """
            SELECT func_post_tags_create(:post_id, :tag_id)
        """
        ),
        {"post_id": post_tag.post_id, "tag_id": post_tag.tag_id},
    ).fetchone()

    message = result[0]

    if message == "Post does not exist":
        raise HTTPException(status_code=404, detail=ErrMsg.POST_NOT_FOUND)
    if message == "Tag does not exist":
        raise HTTPException(status_code=404, detail=ErrMsg.TAG_NOT_FOUND)
    if message == "Post already has this tag":
        raise HTTPException(status_code=400, detail=ErrMsg.POST_TAG_EXISTS)

    db.commit()
    return {"message": message}


def get_post_tags(db: Session, post_id: int):
    result = (
        db.execute(
            text("SELECT * FROM func_post_tags_read_by_post(:post_id)"),
            {"post_id": post_id},
        )
        .mappings()
        .fetchall()
    )
    return [dict(row) for row in result]


def get_posts_by_tag(db: Session, tag_id: int):
    result = (
        db.execute(
            text("SELECT * FROM func_post_tags_read_by_tag(:tag_id)"),
            {"tag_id": tag_id},
        )
        .mappings()
        .fetchall()
    )
    return [dict(row) for row in result]


def delete_post_tag(db: Session, post_id: int, tag_id: int):
    result = db.execute(
        text("SELECT func_post_tags_delete(:post_id, :tag_id)"),
        {"post_id": post_id, "tag_id": tag_id},
    ).fetchone()

    message = result[0]

    if message == "Post-Tag relation does not exist":
        raise HTTPException(status_code=404, detail=ErrMsg.POST_TAG_NOT_FOUND)

    db.commit()
    return {"message": message}

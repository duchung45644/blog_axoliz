from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException

from app.schemas.comments_schema import CommentCreate, CommentUpdate


def create_comment(db: Session, comment: CommentCreate):
    try:
        result = db.execute(
            text(
                """
                SELECT func_comments_create(:post_id, :user_id, :content, :parent_comment_id)
            """
            ),
            {
                "post_id": comment.post_id,
                "user_id": comment.user_id,
                "content": comment.content,
                "parent_comment_id": comment.parent_comment_id,
            },
        ).fetchone()

        db.commit()
        return {"message": "Comment created successfully", "comment_id": result[0]}

    except Exception as e:
        if "Post does not exist" in str(e):
            raise HTTPException(status_code=404, detail="Post not found")
        if "Parent comment does not exist" in str(e):
            raise HTTPException(status_code=404, detail="Parent comment not found")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


def get_comments_by_post(db: Session, post_id: int):
    result = (
        db.execute(
            text("SELECT * FROM func_comments_read_by_post(:post_id)"),
            {"post_id": post_id},
        )
        .mappings()
        .fetchall()
    )
    return [dict(row) for row in result]


def get_comment_by_id(db: Session, comment_id: int):
    result = (
        db.execute(
            text("SELECT * FROM func_comments_read_by_id(:id)"), {"id": comment_id}
        )
        .mappings()
        .fetchone()
    )
    if not result:
        raise HTTPException(status_code=404, detail="Comment not found")

    return dict(result)


def update_comment(db: Session, comment_id: int, comment: CommentUpdate):
    try:
        db.execute(
            text("SELECT func_comments_update(:id, :content)"),
            {"id": comment_id, "content": comment.content},
        )
        db.commit()
        return {"message": "Comment updated successfully"}

    except Exception as e:
        error_message = str(e)
        if "Comment not found" in error_message:
            raise HTTPException(status_code=404, detail="Comment not found")
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )


def delete_comment(db: Session, comment_id: int):
    try:
        db.execute(text("SELECT func_comments_delete(:id)"), {"id": comment_id})
        db.commit()
        return {"message": "Comment deleted successfully"}

    except Exception as e:
        error_message = str(e)
        if "Comment not found" in error_message:
            raise HTTPException(status_code=404, detail="Comment not found")
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )

import psycopg2
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException

from app.constants import ErrorMessages as ErrMsg
from app.schemas.posts_schema import PostCreate, PostUpdate


def create_post(db: Session, post: PostCreate):
    try:
        result = db.execute(
            text(
                """
                SELECT func_posts_create(
                    :user_id, 
                    :title, 
                    :slug, 
                    :content, 
                    :featured_image, 
                    :is_published, 
                    :youtube_video_url,
                    :category_id
                )
            """
            ),
            {
                "user_id": post.user_id,
                "title": post.title,
                "slug": post.slug,
                "content": post.content,
                "featured_image": post.featured_image,
                "is_published": post.is_published,
                "youtube_video_url": post.youtube_video_url,
                "category_id": post.category_id,
            },
        ).fetchone()

        db.commit()
        return get_post_by_id(db, result[0])

    except Exception as e:
        error_message = str(e)
        if "User does not exist" in error_message:
            raise HTTPException(status_code=404, detail=ErrMsg.USER_NOT_FOUND)
        if "Category does not exist" in error_message:
            raise HTTPException(status_code=404, detail=ErrMsg.CATEGORY_NOT_FOUND)
        if "Post slug already exists" in error_message:
            raise HTTPException(status_code=400, detail=ErrMsg.POST_SLUG_EXISTS)

        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )


def get_post_by_id(db: Session, post_id: int):
    result = (
        db.execute(
            text("SELECT * FROM func_posts_read_by_id(:post_id)"), {"post_id": post_id}
        )
        .mappings()
        .fetchone()
    )

    if not result:
        raise HTTPException(status_code=404, detail=ErrMsg.POST_NOT_FOUND)

    return result


def get_all_posts(
    db: Session,
    limit: int = 10,
    offset: int = 0,
    search: str = None,
    category_id: int = None,
    is_published: bool = None,
):
    try:
        result = (
            db.execute(
                text(
                    """
                SELECT * FROM func_posts_read_all(
                    :limit, 
                    :offset, 
                    :search, 
                    :category_id, 
                    :is_published
                )
            """
                ),
                {
                    "limit": limit,
                    "offset": offset,
                    "search": search,
                    "category_id": category_id,
                    "is_published": is_published,
                },
            )
            .mappings()
            .all()
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


def search_posts(db: Session, query: str, limit: int = 10, offset: int = 0):
    try:
        result = (
            db.execute(
                text(
                    """
                SELECT * FROM func_posts_search(:query, :limit, :offset)
            """
                ),
                {"query": query, "limit": limit, "offset": offset},
            )
            .mappings()
            .all()
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


def update_post(db: Session, post_id: int, post: PostUpdate):

    post_exists = db.execute(
        text("SELECT EXISTS(SELECT 1 FROM posts WHERE id = :post_id)"),
        {"post_id": post_id},
    ).scalar()

    if not post_exists:
        raise HTTPException(status_code=404, detail="Post not found")

    try:
        db.execute(
            text(
                """
                SELECT func_posts_update(
                    :post_id, 
                    :title, 
                    :slug, 
                    :content, 
                    :featured_image, 
                    :is_published, 
                    :youtube_video_url,
                    :category_id
                )
            """
            ),
            {
                "post_id": post_id,
                "title": post.title,
                "slug": post.slug,
                "content": post.content,
                "featured_image": post.featured_image,
                "is_published": post.is_published,
                "youtube_video_url": post.youtube_video_url,
                "category_id": (
                    post.category_id if post.category_id is not None else None
                ),
            },
        )
        db.commit()
        return get_post_by_id(db, post_id)

    except Exception as e:
        error_message = str(e)
        if "Post not found" in error_message:
            raise HTTPException(status_code=404, detail=ErrMsg.POST_NOT_FOUND)

        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )


def delete_post(db: Session, post_id: int):

    post_exists = db.execute(
        text("SELECT EXISTS(SELECT 1 FROM posts WHERE id = :post_id)"),
        {"post_id": post_id},
    ).scalar()

    if not post_exists:
        raise HTTPException(status_code=404, detail=ErrMsg.POST_NOT_FOUND)

    try:
        db.execute(text("SELECT func_posts_delete(:post_id)"), {"post_id": post_id})
        db.commit()
        return {"message": "Post deleted successfully"}

    except Exception as e:
        error_message = str(e)
        if "Post not found" in error_message:
            raise HTTPException(status_code=404, detail=ErrMsg.POST_NOT_FOUND)

        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )

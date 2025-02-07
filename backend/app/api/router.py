from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    users,
    posts,
    tags,
    categories,
    comments,
    post_tags,
)

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
api_router.include_router(post_tags.router, prefix="/post_tags", tags=["post_tags"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])

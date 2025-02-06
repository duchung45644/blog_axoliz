from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException

from app.schemas.tags_schema import TagCreate, TagUpdate


def create_tag(db: Session, tag: TagCreate):
    try:
        result = db.execute(
            text(
                """
                SELECT func_tags_create(:name, :slug)
            """
            ),
            {"name": tag.name, "slug": tag.slug},
        ).fetchone()

        db.commit()

        new_tag_id = result[0]
        return get_tag_by_id(db, new_tag_id)

    except Exception as e:
        if "Tag name already exists" in str(e):
            raise HTTPException(status_code=400, detail="Tag name already exists")
        if "Tag slug already exists" in str(e):
            raise HTTPException(status_code=400, detail="Tag slug already exists")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


def get_tags(db: Session):
    result = db.execute(text("SELECT * FROM func_tags_read_all()")).fetchall()
    return [dict(row._mapping) for row in result]


def get_tag_by_id(db: Session, tag_id: int):
    result = (
        db.execute(text("SELECT * FROM func_tags_read_by_id(:id)"), {"id": tag_id})
        .mappings()
        .fetchone()
    )

    if not result:
        raise HTTPException(status_code=404, detail="Tag not found")

    return dict(result)


def update_tag(db: Session, tag_id: int, tag: TagUpdate):
    try:
        db.execute(
            text(
                """
                SELECT func_tags_update(:id, :name, :slug)
            """
            ),
            {"id": tag_id, "name": tag.name, "slug": tag.slug},
        )
        db.commit()

        return get_tag_by_id(db, tag_id)

    except Exception as e:
        if "Tag name already exists" in str(e):
            raise HTTPException(status_code=400, detail="Tag name already exists")
        if "Tag slug already exists" in str(e):
            raise HTTPException(status_code=400, detail="Tag slug already exists")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


def delete_tag(db: Session, tag_id: int):
    try:
        db.execute(text("SELECT func_tags_delete(:id)"), {"id": tag_id})
        db.commit()
        return {"message": "Tag deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

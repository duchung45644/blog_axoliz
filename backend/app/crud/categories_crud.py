from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException

from app.schemas.categories_schema import CategoryCreate, CategoryUpdate


def create_category(db: Session, category: CategoryCreate):
    try:
        result = db.execute(
            text(
                """
                SELECT func_categories_create(:name, :slug, :description)
            """
            ),
            {
                "name": category.name,
                "slug": category.slug,
                "description": category.description,
            },
        ).fetchone()

        db.commit()
        return {"message": "Category created successfully", "category_id": result[0]}

    except Exception as e:
        if "Category name already exists" in str(e):
            raise HTTPException(status_code=400, detail="Category name already exists")
        if "Category slug already exists" in str(e):
            raise HTTPException(status_code=400, detail="Category slug already exists")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


def get_categories(db: Session):
    result = (
        db.execute(text("SELECT * FROM func_categories_read_all()"))
        .mappings()
        .fetchall()
    )
    return [dict(row) for row in result]


def get_category_by_id(db: Session, category_id: int):
    result = (
        db.execute(
            text("SELECT * FROM func_categories_read_by_id(:id)"), {"id": category_id}
        )
        .mappings()
        .fetchone()
    )

    if not result:
        raise HTTPException(status_code=404, detail="Category not found")

    return dict(result)


def update_category(db: Session, category_id: int, category: CategoryUpdate):
    try:
        db.execute(
            text(
                """
                SELECT func_categories_update(:id, :name, :slug, :description)
            """
            ),
            {
                "id": category_id,
                "name": category.name,
                "slug": category.slug,
                "description": category.description,
            },
        )
        db.commit()
        return {"message": "Category updated successfully"}

    except Exception as e:
        error_message = str(e)
        if "Category name already exists" in error_message:
            raise HTTPException(status_code=400, detail="Category name already exists")
        if "Category slug already exists" in error_message:
            raise HTTPException(status_code=400, detail="Category slug already exists")
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )


def delete_category(db: Session, category_id: int):
    try:
        result = db.execute(
            text("SELECT func_categories_delete(:id)"), {"id": category_id}
        ).fetchone()

        db.commit()
        return {"message": "Category deleted successfully"}

    except Exception as e:
        error_message = str(e)
        if "Category not found" in error_message:
            raise HTTPException(status_code=404, detail="Category not found")
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {error_message}"
        )

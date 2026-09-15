from fastapi import APIRouter, HTTPException
from bd_users import engine
from sqlalchemy import text

router = APIRouter()


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                DELETE FROM users_base
                WHERE id = :user_id
                RETURNING *
            """),
            {"user_id": user_id},
        )
        delete = result.fetchone()
        if delete is None:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден!"
            )
from fastapi import APIRouter, HTTPException
from bd_users import engine
from sqlalchemy import text

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT id, first_name, last_name, age
                FROM users_base
                WHERE id = :user_id
            """),
            {"user_id": user_id},
        )
        get = result.fetchone()
        if get is None:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден"
            )
        
        return dict(get._mapping)

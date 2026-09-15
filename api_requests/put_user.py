from fastapi import APIRouter, HTTPException
from bd_users import engine
from sqlalchemy import text
from model import UserUpdate

router = APIRouter()

@router.put("/users/{user_id}")
def put_user(user_id: int, user: UserUpdate):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                UPDATE users_base
                SET
                    first_name = :first_name,
                    last_name = :last_name,
                    age = :age
                WHERE id = :user_id
                RETURNING *
            """),
            {
                "user_id": user_id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
            },
        )
        put = result.fetchone()
        if put is None:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден!"
            )
            
        return dict(put._mapping)
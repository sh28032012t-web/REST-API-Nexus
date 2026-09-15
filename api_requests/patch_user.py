from fastapi import APIRouter, HTTPException
from bd_users import engine
from sqlalchemy import text
from model import UserPatch

router = APIRouter()

@router.patch("/users/{user_id}")
def patch_user(user_id: int, user: UserPatch):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                UPDATE users_base
                SET
                    first_name = COALESCE(:first_name, first_name),
                    last_name = COALESCE(:last_name, last_name),
                    age = COALESCE(:age, age)
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
        patch = result.fetchone()
        if patch is None:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден!"
            )
            
        return dict(patch._mapping)
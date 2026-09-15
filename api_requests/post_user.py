from fastapi import APIRouter
from bd_users import engine
from sqlalchemy import text
from model import UserCreate

router = APIRouter()

@router.post("/users", status_code=201)
def post_user(user: UserCreate):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                INSERT INTO users_base (first_name, last_name, age)
                VALUES (:first_name, :last_name, :age)
                RETURNING *
            """),
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
            },
        )
        post = result.fetchone()
        
        return dict(post._mapping)
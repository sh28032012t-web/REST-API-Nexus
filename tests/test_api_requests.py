from api_requests.get_user import get_user
import api_requests.get_user as get_module

from api_requests.post_user import post_user
import api_requests.post_user as post_module

from api_requests.put_user import put_user
import api_requests.put_user as put_module

from api_requests.patch_user import patch_user
import api_requests.patch_user as patch_module

from api_requests.delete_user import delete_user
import api_requests.delete_user as delete_module

from bd_users import engine
from test_bd_users import test_engine
from model import UserCreate, UserUpdate

from sqlalchemy import text



def test_get():
    get_module.engine = test_engine
    
    user_id = 41
    
    user = get_user(user_id)
    
    with test_engine.begin() as connection:
        result = connection.execute(
            text("""
                SELECT *
                FROM users_base
                WHERE id = :user_id
            """),
            {"user_id": user_id}
        )
        
        test_user = result.fetchone()
    
    assert test_user is not None
    assert user == dict(test_user._mapping)


def test_post():
    post_module.engine = test_engine
    
    user = UserCreate(
        first_name="Test",
        last_name="User",
        age=20
    )
    
    created_user = post_user(user)
    
    with test_engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT *
                FROM users_base
                WHERE id = :user_id
            """),
            {"user_id": created_user["id"]}
        )
        test_user = result.fetchone()
        
    assert test_user is not None
    assert created_user == dict(test_user._mapping)
    
    with test_engine.begin() as connection:
        result_exit = connection.execute(
            text("""
                DELETE FROM users_base
                WHERE id = :user_id
            """),
            {"user_id": created_user["id"]}
        )
        
    assert result_exit.rowcount == 1


def test_put():
    put_module.engine = test_engine
    
    with test_engine.begin() as connection:
        result_1 = connection.execute(
            text("""
                SELECT *
                FROM users_base
                WHERE id = 41
            """)
        )
        test_user_1 = result_1.fetchone()
        
        old_user = dict(test_user_1._mapping)
        
    user = UserUpdate(
        first_name="2",
        last_name="Put",
        age=2
    )
    
    new_user = put_user(41, user)
    
    assert new_user != old_user
    
    with test_engine.begin() as connection:
        result_3 = connection.execute(
            text("""
                UPDATE users_base
                SET
                    first_name = :first_name,
                    last_name = :last_name,
                    age = :age
                WHERE id = 41
                RETURNING *
            """),
            {
                "first_name": old_user["first_name"],
                "last_name": old_user["last_name"],
                "age": old_user["age"],
            },
        )
        test_user_3 = result_3.fetchone()
        
        return_user = dict(test_user_3._mapping)
        
        assert return_user == old_user


def test_patch():
    patch_module.engine = test_engine
    
    with test_engine.begin() as connection:
        result_1 = connection.execute(
            text("""
                SELECT *
                FROM users_base
                WHERE id = 41
            """)
        )
        test_user_1 = result_1.fetchone()
        
        old_user = dict(test_user_1._mapping)
        
    user = UserUpdate(
        first_name="2",
        last_name="Put",
        age=2
    )
    
    new_user = patch_user(41, user)
    
    assert new_user != old_user
    
    with test_engine.begin() as connection:
        result_3 = connection.execute(
            text("""
                UPDATE users_base
                SET
                    first_name = COALESCE(:first_name, first_name),
                    last_name = COALESCE(:last_name, last_name),
                    age = COALESCE(:age, age)
                WHERE id = 41
                RETURNING *
            """),
            {
                "first_name": old_user["first_name"],
                "last_name": old_user["last_name"],
                "age": old_user["age"],
            },
        )
        test_user_3 = result_3.fetchone()
        
        return_user = dict(test_user_3._mapping)
        
        assert return_user == old_user


def test_delete():
    delete_module.engine = test_engine
    
    with test_engine.begin() as connection:
        result_1 = connection.execute(
            text("""
                SELECT *
                FROM users_base
                WHERE id = 41
            """)
        )
        test_user_1 = result_1.fetchone()
        
        save_user = dict(test_user_1._mapping)
        
        delete = delete_user(41)
        
        assert delete == None
        
    with test_engine.begin() as connection:
        result_3 = connection.execute(
            text("""
                INSERT INTO users_base (id, first_name, last_name, age)
                OVERRIDING SYSTEM VALUE
                VALUES (:id, :first_name, :last_name, :age)
                RETURNING *
            """),
            {
                "id": save_user["id"],
                "first_name": save_user["first_name"],
                "last_name": save_user["last_name"],
                "age": save_user["age"],
            }
        )
        test_user_2 = result_3.fetchone()
        
        return_user = dict(test_user_2._mapping)
        
        assert return_user == save_user
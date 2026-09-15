from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

TEST_BD_USER = os.getenv("TEST_BD_USER")
TEST_BD_PASSWORD = os.getenv("TEST_BD_PASSWORD")
TEST_BD_HOST = os.getenv("TEST_BD_HOST")
TEST_BD_PORT = os.getenv("TEST_BD_PORT")
TEST_BD_DATABASE = os.getenv("TEST_BD_DATABASE")

test_engine = create_engine(
    f"postgresql+psycopg://{TEST_BD_USER}:{TEST_BD_PASSWORD}@{TEST_BD_HOST}:{TEST_BD_PORT}/{TEST_BD_DATABASE}"
)
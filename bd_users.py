from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

BD_USER = os.getenv("BD_USER")
BD_PASSWORD = os.getenv("BD_PASSWORD")
BD_HOST = os.getenv("BD_HOST")
BD_PORT = os.getenv("BD_PORT")
BD_DATABASE = os.getenv("BD_DATABASE")

engine = create_engine(
    f"postgresql+psycopg://{BD_USER}:{BD_PASSWORD}@{BD_HOST}:{BD_PORT}/{BD_DATABASE}"
)
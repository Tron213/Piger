from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
engine = create_engine(
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@Postgres_piger:5432/{DB_NAME}"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT current_database()"))
    print(result.scalar())
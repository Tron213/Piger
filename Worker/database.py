from sqlalchemy import create_engine
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm import sessionmaker
from Shared.models import Monitor

load_dotenv(find_dotenv())

DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
engine = create_engine(
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@Postgres_piger:5432/{DB_NAME}"
)

SessionLocal = sessionmaker(bind=engine)





def get_active_monitors():
    with SessionLocal() as session:
        return(session.query(Monitor.uuid, Monitor.host).filter(Monitor.enabled == True).all())
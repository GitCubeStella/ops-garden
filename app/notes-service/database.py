from sqlmodel import SQLModel, Session, create_engine
import os

engine = None

def get_engine():
    global engine
    if engine is None:
        DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
        engine = create_engine(DATABASE_URL, echo=True)
    return engine

def get_session():
    session = Session(get_engine())
    try:
        yield session
    finally:
        session.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())

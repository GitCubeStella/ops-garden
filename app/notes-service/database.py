import os
from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager  # <- optional, aber nicht notwendig

engine = None

def get_engine():
    global engine
    if engine is None:
        DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
        engine = create_engine(DATABASE_URL, echo=True)
    return engine

def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session  # <-- wichtig: 'yield' statt 'return'

def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())

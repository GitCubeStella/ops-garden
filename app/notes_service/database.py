from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool
import os

engine = None


def get_engine():
    global engine
    if engine is None:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            host = os.getenv("DB_HOST")
            port = os.getenv("DB_PORT")
            name = os.getenv("DB_NAME")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            if all([host, port, name, user, password]):
                database_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
            else:
                database_url = "sqlite:///./test.db"
        if database_url.startswith("sqlite"):
            kwargs = {"echo": True, "connect_args": {"check_same_thread": False}}
            if database_url.endswith(":memory:"):
                kwargs["poolclass"] = StaticPool
            engine = create_engine(database_url, **kwargs)
        else:
            engine = create_engine(database_url, echo=True)
    return engine

def get_session():
    session = Session(get_engine())
    try:
        yield session
    finally:
        session.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())

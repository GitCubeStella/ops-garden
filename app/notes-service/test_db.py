from sqlmodel import SQLModel, create_engine, Session
from main import app, get_session

# In-Memory SQLite DB für Tests
DATABASE_URL = "sqlite://"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# eigene Session-Factory für Tests
def override_get_session():
    with Session(engine) as session:
        yield session

# Tabellen vor jedem Test anlegen
def create_test_db():
    SQLModel.metadata.create_all(engine)

# Dependency Override setzen
app.dependency_overrides[get_session] = override_get_session

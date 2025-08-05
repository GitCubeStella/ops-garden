from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from main import app
from models import Note
from database import get_session

# 🔧 Eigenen Test-Engine anlegen – dieselbe DB, dieselbe Connection!
test_engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(test_engine)

# 👉 Test-Session-Dependency
def override_get_session():
    with Session(test_engine) as session:
        yield session

# 🔁 Dependency override aktivieren
app.dependency_overrides[get_session] = override_get_session

client = TestClient(app)

def test_create_and_get_note():
    note = {"title": "Testnote", "content": "Das ist nur ein Test"}
    response = client.post("/notes", json=note)
    assert response.status_code == 200
    assert response.json()["title"] == "Testnote"

    # Check ob Note über GET auch abrufbar ist
    get_response = client.get("/notes")
    assert get_response.status_code == 200
    assert len(get_response.json()) > 0

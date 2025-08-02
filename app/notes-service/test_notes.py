from fastapi.testclient import TestClient
from main import app
from database import create_db_and_tables

client = TestClient(app)

def setup_module(module):
    # wird automatisch vor allen Tests im Modul aufgerufen
    create_db_and_tables()

def test_create_and_get_note():
    note = {"title": "Testnote", "content": "Das ist nur ein Test"}
    response = client.post("/notes", json=note)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Testnote"

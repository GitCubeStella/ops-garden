from fastapi.testclient import TestClient
from main import app
from test_db import create_test_db

client = TestClient(app)

def setup_module():
    # wird einmal pro Datei aufgerufen
    create_test_db()

def test_create_and_get_note():
    note = {"title": "Testnote", "content": "Das ist nur ein Test"}
    response = client.post("/notes", json=note)
    assert response.status_code == 200
    created = response.json()
    assert created["title"] == note["title"]

    note_id = created["id"]
    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 200
    assert get_response.json()["content"] == note["content"]

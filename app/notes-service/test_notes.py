from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_note():
    # Notiz anlegen
    note = {"title": "Testnote", "content": "Das ist nur ein Test"}
    response = client.post("/notes", json=note)
    assert response.status_code == 200

    created = response.json()
    assert created["title"] == note["title"]
    assert created["content"] == note["content"]

    note_id = created["id"]

    # Notiz abrufen
    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 200
    fetched = get_response.json()
    assert fetched["title"] == note["title"]
    assert fetched["content"] == note["content"]

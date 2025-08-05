def test_in_memory_sqlite(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    from importlib import reload
    import database
    reload(database)
    import main
    reload(main)
    from fastapi.testclient import TestClient
    with TestClient(main.app) as client:
        note = {"title": "MemTest", "content": "Using memory"}
        response = client.post("/notes_service", json=note)
        assert response.status_code == 200
        assert response.json()["title"] == "MemTest"
        get_response = client.get("/notes_service")
        assert get_response.status_code == 200
        assert len(get_response.json()) == 1
    database.engine = None

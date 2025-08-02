# app/notes-service/test_db.py
from database import get_session, create_db_and_tables
from models import Note

def test_db_inserts_note():
    create_db_and_tables()  # wichtig für In-Memory-DB
    note = Note(title="Eintrag", content="Testeintrag")
    with get_session() as session:
        session.add(note)
        session.commit()
        session.refresh(note)
        assert note.id is not None

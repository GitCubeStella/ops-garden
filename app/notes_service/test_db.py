# app/notes_service-service/test_db.py
from database import get_session, create_db_and_tables
from models import Note

def test_db_inserts_note():
    create_db_and_tables()  # wichtig für SQLite oder In-Memory
    note = Note(title="Eintrag", content="Testeintrag")
    session_gen = get_session()
    session = next(session_gen)
    try:
        session.add(note)
        session.commit()
        session.refresh(note)
        assert note.id is not None
    finally:
        session_gen.close()

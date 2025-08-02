from sqlmodel import select
from database import create_db_and_tables, get_session
from models import Note

def setup_module(module):
    create_db_and_tables()

def test_db_inserts_note():
    note = Note(title="Eintrag", content="Testeintrag")
    with get_session() as session:
        session.add(note)
        session.commit()

        result = session.exec(select(Note)).first()
        assert result.title == "Eintrag"

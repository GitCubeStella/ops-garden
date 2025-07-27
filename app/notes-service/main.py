# app/notes-service/main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import select, Session
from typing import List

from models import Note
from database import create_db_and_tables, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/notes", response_model=List[Note])
def get_notes(session: Session = Depends(get_session)):
    return session.exec(select(Note)).all()

@app.post("/notes", response_model=Note)
def create_note(note: Note, session: Session = Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

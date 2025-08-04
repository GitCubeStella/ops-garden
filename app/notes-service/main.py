from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlmodel import SQLModel, Session, select
from contextlib import asynccontextmanager

from database import get_session, create_db_and_tables
from models import Note
from typing import List


# Lifespan-Ersatz für on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield  # → Startup done; App läuft jetzt


app = FastAPI(lifespan=lifespan)


@app.get("/", include_in_schema=False)
def root_redirect():
    return RedirectResponse(url="/docs")


@app.get("/notes", response_model=List[Note])
def get_notes(session: Session = Depends(get_session)):
    return session.exec(select(Note)).all()


@app.post("/notes", response_model=Note)
def create_note(note: Note, session: Session = Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

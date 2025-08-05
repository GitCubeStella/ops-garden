from fastapi import FastAPI, Depends
from sqlmodel import Session
from .db import create_db_and_tables, engine
from .schemas import UserCreate
from .crud import create_user

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def read_root():
    return {"message": "User service is running"}

@app.post("/users")
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    new_user = create_user(user, session)
    return new_user

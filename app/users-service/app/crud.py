from sqlmodel import Session
from .models import User
from .schemas import UserCreate

def create_user(user: UserCreate, session: Session) -> User:
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

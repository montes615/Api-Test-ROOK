from app.db import engine
from app.db.schemas import User
from sqlmodel import Session


class AuthModel():
    
    def __init__(self) -> None:
        pass
    
    
    def add_user(self, username: str, hashed_password: str) -> None:
        with Session(engine) as session:
            user = User(username=username, hashed_password=hashed_password)
            session.add(user)
            session.commit()
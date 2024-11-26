from app.db import engine
from app.db.schemas import User
from sqlmodel import Session, select


class AuthModel():
    
    def __init__(self) -> None:
        pass
    
    
    def add_user(self, username: str, hashed_password: str) -> None:
        '''Add the user on the DB'''
        with Session(engine) as session:
            user = User(username=username, hashed_password=hashed_password)
            session.add(user)
            session.commit()


    def get_user(self, username: str) -> User:
        '''Gets the user of the DB'''
        with Session(engine) as session:
            statement = select(User).where(User.username == username)
            return session.exec(statement).first()
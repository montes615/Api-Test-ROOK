from app.db import engine
from app.db.schemas import User
from sqlmodel import Session, select
from fastapi import HTTPException, status


class AuthModel():
    
    def __init__(self) -> None:
        pass
    
    
    def add_user(self, username: str, hashed_password: str, usage: str) -> User:
        '''
        Add the user on the DB

        ### Params
            username (str): Username
            hashed_password (str): Hashed user password
            usage (str): User permisons

        ### Raises
            HTTPException: Duplicated username
        '''
        with Session(engine) as session:
            statement = select(User).where(User.username == username)
            register_user = session.exec(statement).first()
            
            if register_user:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='The username alredy exists')
            
            user = User(username=username, hashed_password=hashed_password, usage=usage)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user


    def get_user(self, username: str) -> User:
        '''
        Gets the user of the DB

        ### Params
            username (str): Username
        '''
        with Session(engine) as session:
            statement = select(User).where(User.username == username)
            return session.exec(statement).first()
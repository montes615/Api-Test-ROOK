from sqlmodel import Session, select
from app.db import engine
from app.db.schemas import User


class HealtyModel():

    def __init__(self):
        pass


    def get_user_by_id(self, user_id: int):
        with Session(engine) as session:
            statement = select(User).where(User.id == user_id)
            return session.exec(statement).one()
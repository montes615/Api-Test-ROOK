from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = 'users'
    
    id: int = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now, sa_column_kwargs={'onupdate': datetime.now})
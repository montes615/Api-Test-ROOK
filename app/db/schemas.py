from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    '''Users db schema'''
    __tablename__ = 'users'
    
    id: int = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    usage: str
    created_at: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now, sa_column_kwargs={'onupdate': datetime.now})

    breed_requests: list["BreedRequests"] = Relationship(back_populates="user")
    
    
class BreedStats(SQLModel, table=True):
    '''Breed stats db schema'''
    __tablename__ = 'breed_stats'
    
    id: int = Field(default=None, primary_key=True)
    breed_name: str
    requests: int = Field(default=1)
    created_at: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now, sa_column_kwargs={'onupdate': datetime.now})
    
    
class BreedRequests(SQLModel, table=True):
    '''Breed request db schema'''
    __tablename__ = 'breed_requests'
    
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    breed_name: str
    detail: str
    request_url: str
    cache: bool
    request_status: int
    created_at: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now, sa_column_kwargs={'onupdate': datetime.now})

    user: Optional[User] = Relationship(back_populates="breed_requests")
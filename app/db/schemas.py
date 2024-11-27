from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Literal

class User(SQLModel, table=True):
    __tablename__ = 'users'
    
    id: int = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    usage: str
    created_at: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now, sa_column_kwargs={'onupdate': datetime.now})
    
    
class BreedStats(SQLModel, table=True):
    __tablename__ = 'breed_stats'
    
    id: int = Field(default=None, primary_key=True)
    breed_name: str
    requests: int = Field(default=1)
    created_at: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now, sa_column_kwargs={'onupdate': datetime.now})
    
    
class BreedRequests(SQLModel, table=True):
    __tablename__ = 'breed_requests'
    
    id: int = Field(default=None, primary_key=True)
    breed_name: str
    detail: str = Field(nullable=True)
    request_url: str = Field(nullable=True)
    cache: bool
    request_status: str = Field(nullable=True)
    created_at: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now, sa_column_kwargs={'onupdate': datetime.now})
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class BreedResponse(BaseModel):
    breed_name: str = Field(description='CEO breed name')
    image: str = Field(description='Image of the CEO')
    
    
class BreedCache(BaseModel):
    image: str = Field(description='Image of the CEO')
    expire: datetime = Field(description='Expire time')
    request_url: str = Field(description='Url request')
    status_code: int = Field(description='Status code of the request')
    
    
class BreedStatsResponse(BaseModel):
    breed: str = Field(description='CEO breed name')
    request_count: int = Field(description='Number of requests')
    
    
class StatsResponse(BaseModel):
    top_breeds: List[BreedStatsResponse] = Field(description='List with the 10 most searched breeds')
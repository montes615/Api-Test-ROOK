from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class BreedResponse(BaseModel):
    breed_name: str = Field(description='CEO breed name')
    image: str = Field(description='Image of the CEO')
    
    
class BreedCache(BaseModel):
    image: str
    expire: datetime
    request_url: str
    status_code: int
    
    
class BreedStatsResponse(BaseModel):
    breed: str
    request_count: int
    
    
class StatsResponse(BaseModel):
    top_breeds: List[BreedStatsResponse]
from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class BreedResponse(BaseModel):
    breed_name: str = Field(description='CEO breed name')
    image: str = Field(description='Image of the CEO')
    
    
class BreedCache(BaseModel):
    image: str
    expire: datetime
    request_url: str
    status: str
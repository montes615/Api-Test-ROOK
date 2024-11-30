from pydantic import BaseModel, Field

class HTTPExceptionModel(BaseModel):
    message: str = Field(description='Error message')
    headers: dict|None
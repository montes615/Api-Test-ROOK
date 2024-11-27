from pydantic import BaseModel, Field
from typing import Literal

class RegisterUser(BaseModel):
    username: str = Field(description='Username')
    password: str = Field(description='Password')
    usage: Literal['dogs_breed_api'] = Field(description='User api type')


class LoginUser(BaseModel):
    username: str = Field(description='Username')
    password: str = Field(description='Password')


class TokenResponse(BaseModel):
    access_token: str = Field(description='Access token')
    usage: Literal['dogs_breed_api'] = Field(description='User api type')


class TokenData(BaseModel):
    username: str = Field(description='Username')
    id: int = Field(description='User identifier')
    usage: Literal['dogs_breed_api'] = Field(description='User api type')
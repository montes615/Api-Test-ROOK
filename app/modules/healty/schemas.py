from pydantic import BaseModel
from typing import Literal


class HealtyObject(BaseModel):
    status: Literal['ok', 'failed']
    message: str
    task_time: float


class HealtyResponse(BaseModel):
    db: HealtyObject
    breed_api: HealtyObject
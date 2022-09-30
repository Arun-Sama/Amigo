from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    Id: int
    Title: str
    Price: int
    Summary: str

    class Config:
        orm_mode = True

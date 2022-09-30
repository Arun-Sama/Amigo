from pydantic import BaseModel
from typing import Optional


class UserDetails(BaseModel):
    num: Optional[int]
    name: str

    class Config:
        orm_mode = True

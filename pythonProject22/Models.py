from pydantic import BaseModel


class CarDetails(BaseModel):
    name: str
    brand: str

    class Config:
        orm_mode = True

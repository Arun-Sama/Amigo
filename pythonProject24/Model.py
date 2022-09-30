from pydantic import BaseModel


class TableDetails(BaseModel):
    name: str


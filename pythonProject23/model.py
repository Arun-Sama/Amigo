from pydantic import BaseModel
from typing import List
# from database import *


class NameDetails(BaseModel):
    name: str

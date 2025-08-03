# schemas.py
from pydantic import BaseModel

class ProductBody(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: float
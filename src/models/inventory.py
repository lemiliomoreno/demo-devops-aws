from pydantic import BaseModel


class CreateInventory(BaseModel):
    name: str
    price: float
    category: str


class GetInventory(BaseModel):
    _id: str
    name: str
    price: float
    category: str

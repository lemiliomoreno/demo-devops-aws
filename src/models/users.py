from pydantic import BaseModel


class CreateUser(BaseModel):
    email: str

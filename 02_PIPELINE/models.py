from pydantic import BaseModel

class Recipee(BaseModel):
    name: str
    ingredients: list[str]
    instructions: list[str]
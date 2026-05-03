from pydantic import BaseModel

class Recipee(BaseModel):
    name: str
    food_description: str
    ingredients: list[str]
    instructions: list[str]
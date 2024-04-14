from typing import List, Optional
from pydantic import BaseModel

class NutritionalInfo(BaseModel):
    calories: float
    fat: float
    protein: float

class Ingredient(BaseModel):
    name: str
    quantity: float
    unit: str

class Recipe(BaseModel):
    title: str
    description: str
    cooking_instructions: str
    ingredients: List[Ingredient]
    nutritional_info: NutritionalInfo

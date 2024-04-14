from typing import List, Optional
from models import Recipe, Ingredient, NutritionalInfo
from fastapi import HTTPException
import json

RECIPES_JSON_FILE = 'recipes.json'

def load_recipes() -> List[Recipe]:
    try:
        with open(RECIPES_JSON_FILE, "r") as f:
            recipes_db = json.load(f)
            if not recipes_db:
                return []
            return [Recipe(**recipe) for recipe in recipes_db]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_recipes(recipes: List[Recipe]):
    with open(RECIPES_JSON_FILE, "w") as f:
        json.dump([recipe.dict() for recipe in recipes], f, indent=4)

def create_recipe(recipe: Recipe) -> Recipe:
    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    return recipe

def read_recipe(recipe_id: int) -> Recipe:
    recipes = load_recipes()
    if recipe_id < 0 or recipe_id >= len(recipes):
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes[recipe_id]

def update_recipe(recipe_id: int, recipe: Recipe) -> Recipe:
    recipes = load_recipes()
    if recipe_id < 0 or recipe_id >= len(recipes):
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipes[recipe_id] = recipe
    save_recipes(recipes)
    return recipe

def delete_recipe(recipe_id: int) -> dict:
    recipes = load_recipes()
    if recipe_id < 0 or recipe_id >= len(recipes):
        raise HTTPException(status_code=404, detail="Recipe not found")
    del recipes[recipe_id]
    save_recipes(recipes)
    return {"message": "Recipe deleted successfully"}

def search_recipes(title: Optional[str] = None, ingredient: Optional[str] = None) -> List[Recipe]:
    recipes = load_recipes()
    if title:
        return [recipe for recipe in recipes if recipe.title == title]
    if ingredient:
        return [recipe for recipe in recipes if ingredient in [i.name for i in recipe.ingredients]]
    return recipes

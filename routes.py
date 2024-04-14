from typing import List, Optional
from fastapi import APIRouter, HTTPException
from models import Recipe, Ingredient, NutritionalInfo
from services import create_recipe, read_recipe, update_recipe, delete_recipe, search_recipes

router = APIRouter()

@router.post("/recipes/", response_model=Recipe, summary="Create a new recipe")
def create_recipe_endpoint(recipe: Recipe):
    return create_recipe(recipe)

@router.get("/recipes/{recipe_id}", response_model=Recipe, summary="Get recipe details by ID")
def read_recipe_endpoint(recipe_id: int):
    return read_recipe(recipe_id)

@router.put("/recipes/{recipe_id}", response_model=Recipe, summary="Update recipe details by ID")
def update_recipe_endpoint(recipe_id: int, recipe: Recipe):
    return update_recipe(recipe_id, recipe)

@router.delete("/recipes/{recipe_id}", summary="Delete recipe by ID")
def delete_recipe_endpoint(recipe_id: int):
    return delete_recipe(recipe_id)

@router.get("/recipes/", response_model=List[Recipe], summary="Search recipes")
def search_recipes_endpoint(title: Optional[str] = None, ingredient: Optional[str] = None):
    return search_recipes(title, ingredient)

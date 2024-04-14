from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_recipe():
    recipe_data = {
        "title": "Spaghetti Carbonara",
        "description": "Classic Italian pasta dish with eggs, cheese, pancetta, and black pepper.",
        "cooking_instructions": "Cook spaghetti. Meanwhile, fry pancetta until crispy. Mix eggs, cheese, and pepper. Combine all ingredients.",
        "ingredients": [
            {"name": "Spaghetti", "quantity": 200, "unit": "g"},
            {"name": "Pancetta", "quantity": 100, "unit": "g"},
            {"name": "Eggs", "quantity": 2, "unit": ""},
            {"name": "Parmesan Cheese", "quantity": 50, "unit": "g"},
            {"name": "Black Pepper", "quantity": 1, "unit": "tsp"}
        ],
        "nutritional_info": {"calories": 500, "fat": 25, "protein": 20}
    }
    response = client.post("/api/recipes/", json=recipe_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Spaghetti Carbonara"

def test_read_recipe():
    response = client.get("/api/recipes/0")
    assert response.status_code == 200
    assert response.json()["title"] == "Spaghetti Carbonara"

def test_update_recipe():
    updated_recipe_data = {
        "title": "Spaghetti Carbonara - Updated",
        "description": "Updated description",
        "cooking_instructions": "Updated cooking instructions",
        "ingredients": [
            {"name": "Spaghetti", "quantity": 250, "unit": "g"},  # Updated quantity
            {"name": "Pancetta", "quantity": 120, "unit": "g"},   # Updated quantity
            {"name": "Eggs", "quantity": 3, "unit": ""},          # Updated quantity
            {"name": "Parmesan Cheese", "quantity": 60, "unit": "g"},  # Updated quantity
            {"name": "Black Pepper", "quantity": 1.5, "unit": "tsp"}    # Updated quantity
        ],
        "nutritional_info": {"calories": 600, "fat": 30, "protein": 25}  # Updated nutritional info
    }
    response = client.put("/api/recipes/0", json=updated_recipe_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Spaghetti Carbonara - Updated"
    assert response.json()["ingredients"][0]["quantity"] == 250

def test_delete_recipe():
    response = client.delete("/api/recipes/0")
    assert response.status_code == 200
    assert response.json()["message"] == "Recipe deleted successfully"

def test_search_recipes_by_title():
    response = client.get("/api/recipes/?title=Spaghetti Carbonara - Updated")
    assert response.status_code == 200
    assert len(response.json()) == 0  # Recipe should be deleted

def test_search_recipes_by_ingredient():
    response = client.get("/api/recipes/?ingredient=Parmesan Cheese")
    assert response.status_code == 200
    assert len(response.json()) == 0  # Recipe should be deleted

def test_search_recipes_no_filter():
    response = client.get("/api/recipes/")
    assert response.status_code == 200
    assert len(response.json()) == 0  # No recipes after deletion


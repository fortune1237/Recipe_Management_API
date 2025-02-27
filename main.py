from fastapi import FastAPI
from routes import router as recipe_router

app = FastAPI()

app.include_router(recipe_router, prefix="/api")

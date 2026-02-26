# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

items = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# TODO: Implement CRUD endpoints for Item
# - POST /items
# - GET /items/{item_id}
# - PUT /items/{item_id}
# - DELETE /items/{item_id}

# Bonus: Add descriptions and examples to endpoints

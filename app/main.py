from fastapi import FastAPI
from .api.routes import app_router

app = FastAPI(title="App API")

app.include_router(app_router)

# Default route
@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
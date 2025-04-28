from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import app_router

app = FastAPI(title="NPTEL Certificate API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(app_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

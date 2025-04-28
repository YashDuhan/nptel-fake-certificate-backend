from fastapi import APIRouter
from .endpoints import get_certificate

app_router = APIRouter()

app_router.get("/certificate")(get_certificate)


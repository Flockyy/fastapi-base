from fastapi import APIRouter

from api.api_v1.endpoints import predictions

api_router = APIRouter()

api_router.include_router(predictions.router, prefix="/prediction", tags=["prediction"])
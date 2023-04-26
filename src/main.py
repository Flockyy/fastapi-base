from fastapi import FastAPI
import uvicorn
from core.config import settings
from api.api_v1.api import api_router

app = FastAPI(
  title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)


from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import List, Optional, Union
import secrets

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SERVER_NAME: str = "localhost:8000"
    PROJECT_NAME: str = "Chatbot API"
    
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///sql.db"
    FIRST_SUPERUSER: EmailStr = "admin@chatbotapi.com"

    class Config:
        case_sensitive = True 
        
settings = Settings()
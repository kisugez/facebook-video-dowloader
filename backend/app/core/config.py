"""Application configuration settings"""
from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # API Settings
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Facebook Video Downloader API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "API for downloading Facebook videos"
    
    # CORS Settings
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # Download Settings
    DOWNLOAD_DIR: Path = Path("downloads")
    MAX_FILE_AGE_SECONDS: int = 3600  # 1 hour
    
    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

# Ensure download directory exists
settings.DOWNLOAD_DIR.mkdir(exist_ok=True)

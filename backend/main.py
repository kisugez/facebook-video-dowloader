"""
DEPRECATED: This file is kept for backward compatibility.
Please use 'python run.py' or 'uvicorn app.main:app' instead.
"""
from app.main import app
from app.core.config import settings

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )


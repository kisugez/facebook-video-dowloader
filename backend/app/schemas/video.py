"""Video-related schemas"""
from typing import Optional, List
from pydantic import BaseModel, HttpUrl, Field


class VideoFormat(BaseModel):
    """Video format information"""
    format_id: str
    resolution: str
    ext: str
    filesize: Optional[int] = None
    format_note: str = ""


class VideoRequest(BaseModel):
    """Request model for video processing"""
    url: HttpUrl = Field(..., description="Facebook video URL")


class VideoResponse(BaseModel):
    """Response model for video processing"""
    success: bool
    message: str
    download_id: Optional[str] = None
    thumbnail_url: Optional[str] = None
    title: Optional[str] = None
    duration: Optional[int] = None
    formats: Optional[List[VideoFormat]] = None


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str

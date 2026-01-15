"""Video-related API routes"""
from fastapi import APIRouter, HTTPException, BackgroundTasks, Query
from fastapi.responses import FileResponse

from app.schemas.video import VideoRequest, VideoResponse
from app.services.video import VideoService
from app.core.logging import logger

router = APIRouter()


@router.post("/process-video", response_model=VideoResponse)
async def process_video(video_request: VideoRequest):
    """
    Process a Facebook video URL and extract information.
    
    This endpoint extracts video metadata without downloading the video.
    Returns video information including available formats, thumbnail, and title.
    """
    try:
        url = str(video_request.url)
        
        # Validate URL
        if not VideoService.validate_facebook_url(url):
            raise HTTPException(status_code=400, detail="Not a valid Facebook URL")
        
        # Extract video info
        video_info = VideoService.extract_video_info(url)
        
        return VideoResponse(
            success=True,
            message="Video processed successfully",
            download_id=video_info['download_id'],
            thumbnail_url=video_info['thumbnail_url'],
            title=video_info['title'],
            duration=video_info['duration'],
            formats=video_info['formats']
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error processing video: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@router.get("/download/{download_id}")
async def download_video(
    download_id: str,
    url: str = Query(..., description="Facebook video URL"),
    format_id: str = Query("best", description="Video format ID"),
    background_tasks: BackgroundTasks = None
):
    """
    Download a Facebook video.
    
    Downloads the video in the specified format and returns it as a file.
    The downloaded file is automatically cleaned up after sending.
    """
    try:
        # Validate download_id
        if not download_id or ".." in download_id or "/" in download_id:
            raise HTTPException(status_code=400, detail="Invalid download ID")
        
        # Validate URL
        if not VideoService.validate_facebook_url(url):
            raise HTTPException(status_code=400, detail="Not a valid Facebook URL")
        
        # Download video
        file_path = VideoService.download_video(url, download_id, format_id)
        
        # Schedule cleanup
        if background_tasks:
            background_tasks.add_task(VideoService.cleanup_download, file_path)
        
        return FileResponse(
            path=str(file_path),
            filename=file_path.name,
            media_type="application/octet-stream"
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error downloading video: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")

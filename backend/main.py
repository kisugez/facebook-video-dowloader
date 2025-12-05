from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, HttpUrl
import yt_dlp
import os
import uuid
import shutil
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Facebook Video Downloader API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

class VideoRequest(BaseModel):
    url: HttpUrl

class VideoResponse(BaseModel):
    success: bool
    message: str
    download_id: str = None
    thumbnail_url: str = None
    title: str = None
    duration: int = None
    formats: list = None

@app.post("/api/process-video", response_model=VideoResponse)
async def process_video(video_request: VideoRequest):
    try:
        url = str(video_request.url)
        

        if "facebook.com" not in url and "fb.com" not in url:
            raise HTTPException(status_code=400, detail="Not a valid Facebook URL")
        download_id = str(uuid.uuid4())
        download_path = DOWNLOAD_DIR / download_id
        download_path.mkdir(exist_ok=True)
        
        ydl_opts = {
            'format': 'best',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'skip_download': True, 
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = []
            if 'formats' in info:
                for format in info.get('formats', []):
                    if format.get('resolution') and format.get('ext'):
                        formats.append({
                            'format_id': format.get('format_id'),
                            'resolution': format.get('resolution'),
                            'ext': format.get('ext'),
                            'filesize': format.get('filesize'),
                            'format_note': format.get('format_note', '')
                        })
            
            
            thumbnail_url = info.get('thumbnail')
            
            return {
                "success": True,
                "message": "Video processed successfully",
                "download_id": download_id,
                "thumbnail_url": thumbnail_url,
                "title": info.get('title', 'Facebook Video'),
                "duration": info.get('duration'),
                "formats": formats
            }
            
    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Download error: {str(e)}")
        return JSONResponse(
            status_code=400,
            content={"success": False, "message": f"Could not process video: {str(e)}"}
        )
    except Exception as e:
        logger.error(f"Error processing video: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": f"Server error: {str(e)}"}
        )

@app.get("/api/download/{download_id}")
async def download_video(download_id: str, format_id: str = "best", background_tasks: BackgroundTasks = None):
    try:
        if not download_id or ".." in download_id or "/" in download_id:
            raise HTTPException(status_code=400, detail="Invalid download ID")
        
        download_path = DOWNLOAD_DIR / download_id
        if not download_path.exists():
            download_path.mkdir(exist_ok=True)
        
        url = request.query_params.get("url")
        if not url:
            raise HTTPException(status_code=400, detail="URL is required")
        
        ydl_opts = {
            'format': format_id if format_id != "best" else 'best',
            'outtmpl': str(download_path / '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            def cleanup_files():
                try:
                    if os.path.exists(filename):
                        os.remove(filename)
                    if download_path.exists():
                        shutil.rmtree(download_path)
                except Exception as e:
                    logger.error(f"Error cleaning up files: {str(e)}")
            
            if background_tasks:
                background_tasks.add_task(cleanup_files)
            
            return FileResponse(
                path=filename,
                filename=os.path.basename(filename),
                media_type="application/octet-stream"
            )
            
    except Exception as e:
        logger.error(f"Error downloading video: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": f"Download failed: {str(e)}"}
        )

@app.get("/api/thumbnail/{download_id}")
async def get_thumbnail(download_id: str):
    return JSONResponse(
        content={"url": f"/placeholder.svg?height=360&width=640&text=Video+{download_id}"}
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

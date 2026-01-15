"""Video download service using yt-dlp"""
import os
import uuid
import shutil
from pathlib import Path
from typing import Dict, Any, Optional
import yt_dlp

from app.core.config import settings
from app.core.logging import logger
from app.schemas.video import VideoFormat


class VideoService:
    """Service for handling video downloads"""
    
    @staticmethod
    def validate_facebook_url(url: str) -> bool:
        """Validate if URL is a Facebook URL"""
        return "facebook.com" in url or "fb.com" in url
    
    @staticmethod
    def extract_video_info(url: str) -> Dict[str, Any]:
        """Extract video information without downloading"""
        if not VideoService.validate_facebook_url(url):
            raise ValueError("Not a valid Facebook URL")
        
        download_id = str(uuid.uuid4())
        download_path = settings.DOWNLOAD_DIR / download_id
        download_path.mkdir(exist_ok=True)
        
        ydl_opts = {
            'format': 'best',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Extract formats
                formats = []
                if 'formats' in info:
                    for fmt in info.get('formats', []):
                        if fmt.get('resolution') and fmt.get('ext'):
                            formats.append(VideoFormat(
                                format_id=fmt.get('format_id', ''),
                                resolution=fmt.get('resolution', ''),
                                ext=fmt.get('ext', ''),
                                filesize=fmt.get('filesize'),
                                format_note=fmt.get('format_note', '')
                            ))
                
                return {
                    'download_id': download_id,
                    'thumbnail_url': info.get('thumbnail'),
                    'title': info.get('title', 'Facebook Video'),
                    'duration': info.get('duration'),
                    'formats': formats
                }
        except yt_dlp.utils.DownloadError as e:
            logger.error(f"yt-dlp download error: {str(e)}")
            # Clean up directory if created
            if download_path.exists():
                shutil.rmtree(download_path)
            raise ValueError(f"Could not process video: {str(e)}")
        except Exception as e:
            logger.error(f"Error extracting video info: {str(e)}")
            # Clean up directory if created
            if download_path.exists():
                shutil.rmtree(download_path)
            raise
    
    @staticmethod
    def download_video(url: str, download_id: str, format_id: str = "best") -> Path:
        """Download video and return file path"""
        download_path = settings.DOWNLOAD_DIR / download_id
        if not download_path.exists():
            download_path.mkdir(exist_ok=True)
        
        ydl_opts = {
            'format': format_id if format_id != "best" else 'best',
            'outtmpl': str(download_path / '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                return Path(filename)
        except Exception as e:
            logger.error(f"Error downloading video: {str(e)}")
            raise
    
    @staticmethod
    def cleanup_download(file_path: Path):
        """Clean up downloaded file and directory"""
        try:
            if file_path.exists():
                os.remove(file_path)
            
            # Remove parent directory if it's in downloads
            parent_dir = file_path.parent
            if parent_dir.exists() and settings.DOWNLOAD_DIR in parent_dir.parents:
                shutil.rmtree(parent_dir)
        except Exception as e:
            logger.error(f"Error cleaning up files: {str(e)}")

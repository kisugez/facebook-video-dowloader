@echo off
REM Start script for the Facebook Video Downloader backend (Windows)

echo.
echo Starting Facebook Video Downloader Backend...
echo.

REM Check if we're in the backend directory
if not exist "requirements.txt" (
    echo Error: Please run this script from the backend directory
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    echo Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
echo Checking dependencies...
pip install -q -r requirements.txt

REM Start the server
echo.
echo Starting FastAPI server on http://localhost:8000
echo API Documentation: http://localhost:8000/api/docs
echo Health Check: http://localhost:8000/health
echo.
echo Press CTRL+C to stop the server
echo.

python run.py

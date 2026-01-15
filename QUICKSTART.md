# Facebook Video Downloader - Quick Start Guide

This guide will help you get the Facebook Video Downloader running on your local machine in just a few minutes.

## 📋 Prerequisites

Make sure you have these installed:
- **Python 3.11+** → [Download](https://www.python.org/downloads/)
- **Node.js 18+** → [Download](https://nodejs.org/)
- **Git** → [Download](https://git-scm.com/)

## 🚀 Quick Setup (5 minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/kisugez/facebook-video-dowloader.git
cd facebook-video-dowloader
```

### Step 2: Start the Backend

#### On macOS/Linux:
```bash
cd backend
chmod +x start.sh
./start.sh
```

#### On Windows:
```bash
cd backend
start.bat
```

#### Or manually:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

✅ Backend should now be running at http://localhost:8000

### Step 3: Start the Frontend (New Terminal)

```bash
# From the project root directory
npm install
npm run dev
```

✅ Frontend should now be running at http://localhost:3000

## 🎥 How to Use

1. Open http://localhost:3000 in your browser
2. Paste a Facebook video URL (e.g., `https://www.facebook.com/watch?v=123456789`)
3. Click "Process Video"
4. Select your preferred quality
5. Click "Download Now"
6. The video will download to your browser's Downloads folder

### Viewing Downloaded Videos

- **In Browser**: Drag and drop the downloaded video into a new browser tab
- **Video Player**: Open with VLC, Windows Media Player, QuickTime, etc.
- **File Location**: Usually in `~/Downloads` or `C:\Users\YourName\Downloads`

## 🔍 Verify Installation

### Check Backend:
```bash
curl http://localhost:8000/health
# Should return: {"status":"healthy","version":"1.0.0"}
```

### Check API Docs:
Open http://localhost:8000/api/docs in your browser

### Check Frontend:
Open http://localhost:3000 in your browser

## 🛠️ Troubleshooting

### Backend Issues

**Error: Port 8000 already in use**
```bash
# Find and stop the process using port 8000
# On macOS/Linux:
lsof -ti:8000 | xargs kill -9
# On Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Error: ModuleNotFoundError**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Issues

**Error: Port 3000 already in use**
```bash
# Kill the process or use a different port
PORT=3001 npm run dev
```

**Error: Cannot connect to backend**
- Make sure backend is running on port 8000
- Check `NEXT_PUBLIC_API_URL` in `.env.local` (should be `http://localhost:8000`)

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the API at http://localhost:8000/api/docs
- Check out the project structure in the README

## ⚠️ Important Notes

- This tool is for **personal use only**
- Respect **copyright laws** and Facebook's Terms of Service
- Downloaded videos are for private viewing only

---

Need help? Check the main [README.md](README.md) or open an issue on GitHub.

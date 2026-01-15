# Facebook Video Downloader

A modern web application that allows users to download videos from Facebook by providing the video URL. Built with FastAPI backend and Next.js frontend.

## ✨ Features

- 📥 Download videos from Facebook with a simple URL
- 🖼️ Preview video thumbnails before downloading
- 🎯 Select video quality/format
- 🎨 Clean, responsive UI with Facebook's blue color scheme
- ⚡ Fast and efficient video processing
- 🔒 Secure and privacy-focused

## 🏗️ Tech Stack

### Frontend
- **Next.js 15** - React framework with server-side rendering
- **React 19** - UI library
- **Tailwind CSS** - Utility-first CSS framework
- **TypeScript** - Type-safe JavaScript
- **Radix UI** - Accessible component library
- **Lucide React** - Beautiful icon library

### Backend
- **FastAPI** - Modern, fast Python web framework
- **yt-dlp** - Powerful video downloader
- **Python 3.11+** - Programming language
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

## 📋 Prerequisites

Before running this application, make sure you have:

- **Python 3.11 or higher** installed ([Download Python](https://www.python.org/downloads/))
- **Node.js 18 or higher** installed ([Download Node.js](https://nodejs.org/))
- **npm** or **pnpm** package manager

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kisugez/facebook-video-dowloader.git
cd facebook-video-dowloader
```

### 2. Setup Backend (FastAPI)

#### Navigate to backend directory
```bash
cd backend
```

#### Create a virtual environment (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Run the backend server
```bash
# Using the run script (recommended)
python run.py

# Or using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or using the old main.py (backward compatible)
python main.py
```

The backend API will be available at:
- **API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs
- **Alternative Docs**: http://localhost:8000/api/redoc
- **Health Check**: http://localhost:8000/health

### 3. Setup Frontend (Next.js)

Open a new terminal window and navigate to the project root:

```bash
# From backend directory, go back to root
cd ..

# Install dependencies
npm install
# or if using pnpm
pnpm install
```

#### Run the development server
```bash
npm run dev
# or
pnpm dev
```

The frontend will be available at:
- **Application**: http://localhost:3000

## 🎥 How to Use

### Downloading a Facebook Video

1. **Open the application** in your browser at http://localhost:3000
2. **Copy a Facebook video URL** (e.g., `https://www.facebook.com/watch?v=123456789`)
3. **Paste the URL** into the input field
4. **Click "Process Video"** button
5. **Wait for processing** - The app will extract video information
6. **Select quality** - Choose your preferred video quality/format
7. **Click "Download Now"** - The video will download to your browser's download folder

### Viewing Downloaded Videos

After downloading:

1. **Check your browser's download folder** (usually `Downloads` directory)
2. **The video file** will be saved with the original Facebook video title
3. **Open with any video player** (VLC, Windows Media Player, QuickTime, etc.)

#### To view in browser:
- Most browsers allow you to **drag and drop** the downloaded video file into a browser tab
- Or use the browser's **"Open File"** option (Ctrl+O / Cmd+O)
- The video will play directly in the browser

## 📁 Project Structure

```
facebook-video-dowloader/
├── backend/                      # FastAPI backend
│   ├── app/                      # Application package
│   │   ├── api/                  # API routes
│   │   │   └── routes/
│   │   │       └── video.py      # Video endpoints
│   │   ├── core/                 # Core functionality
│   │   │   ├── config.py         # Configuration settings
│   │   │   └── logging.py        # Logging setup
│   │   ├── schemas/              # Pydantic models
│   │   │   └── video.py          # Video schemas
│   │   ├── services/             # Business logic
│   │   │   └── video.py          # Video service
│   │   └── main.py               # FastAPI app initialization
│   ├── downloads/                # Downloaded videos (temporary)
│   ├── requirements.txt          # Python dependencies
│   ├── run.py                    # Application entry point
│   ├── main.py                   # Legacy entry point
│   └── Dockerfile                # Docker configuration
├── app/                          # Next.js app directory
│   ├── page.tsx                  # Home page
│   ├── layout.tsx                # Root layout
│   ├── actions.ts                # Server actions
│   └── globals.css               # Global styles
├── components/                   # React components
│   ├── video-downloader.tsx      # Main downloader component
│   └── ui/                       # UI components
├── public/                       # Static files
├── package.json                  # Node.js dependencies
└── README.md                     # This file
```

## 🔧 Configuration

### Backend Configuration

The backend can be configured via environment variables. Create a `.env` file in the `backend` directory:

```env
# API Settings
API_V1_STR=/api
PROJECT_NAME=Facebook Video Downloader API
VERSION=1.0.0

# CORS Settings
BACKEND_CORS_ORIGINS=["http://localhost:3000"]

# Server Settings
HOST=0.0.0.0
PORT=8000
RELOAD=True
```

### Frontend Configuration

Set the backend API URL in your environment. Create a `.env.local` file in the root directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🐛 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'app'`
- **Solution**: Make sure you're running from the `backend` directory and have activated the virtual environment

**Problem**: `Port 8000 already in use`
- **Solution**: Change the port in the configuration or kill the process using port 8000

**Problem**: `yt-dlp download error`
- **Solution**: Update yt-dlp to the latest version: `pip install --upgrade yt-dlp`

### Frontend Issues

**Problem**: `ECONNREFUSED` or connection errors
- **Solution**: Make sure the backend server is running on port 8000

**Problem**: CORS errors
- **Solution**: Verify that `http://localhost:3000` is in the `BACKEND_CORS_ORIGINS` configuration

## 🔒 Privacy & Legal

- This tool is for **personal use only**
- Please **respect copyright laws** and Facebook's Terms of Service
- Downloaded videos should not be redistributed without permission
- The application does not store or track any user data
- All downloads are temporary and automatically cleaned up

## 🛠️ Development

### Running Tests

```bash
# Backend tests (if available)
cd backend
pytest

# Frontend tests (if available)
npm test
```

### Code Quality

```bash
# Frontend linting
npm run lint

# Backend linting (requires additional tools)
cd backend
flake8 app/
black app/
mypy app/
```

## 📝 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

### Main Endpoints

#### POST `/api/process-video`
Process a Facebook video URL and extract metadata.

**Request Body**:
```json
{
  "url": "https://www.facebook.com/watch?v=123456789"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Video processed successfully",
  "download_id": "uuid-here",
  "thumbnail_url": "https://...",
  "title": "Video Title",
  "duration": 120,
  "formats": [...]
}
```

#### GET `/api/download/{download_id}`
Download the processed video.

**Query Parameters**:
- `url`: Facebook video URL (required)
- `format_id`: Format ID to download (default: "best")

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available for personal use.

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video download functionality
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [Next.js](https://nextjs.org/) - Frontend framework

---

Made with ❤️ for video enthusiasts

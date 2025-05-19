# Facebook Video Downloader

A web application that allows users to download videos from Facebook by providing the video URL.

## Features

- Download videos from Facebook
- Preview video thumbnails before downloading
- Select video quality/format
- Clean, responsive UI with Facebook's blue color scheme
- Quicksand font for a modern look

## Tech Stack

### Frontend
- Next.js 14
- React
- Tailwind CSS
- TypeScript

### Backend
- FastAPI
- yt-dlp (for video downloading)
- Python 3.11+

## Setup Instructions

### Prerequisites
- Node.js 18+
- Python 3.11+
- npm or yarn
- pip

### Backend Setup

1. Navigate to the backend directory:
   \`\`\`
   cd backend
   \`\`\`

2. Create a virtual environment:
   \`\`\`
   python -m venv venv
   \`\`\`

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

5. Start the FastAPI server:
   \`\`\`
   uvicorn main:app --reload
   \`\`\`

The backend will be running at http://localhost:8000

### Frontend Setup

1. Install dependencies:
   \`\`\`
   npm install
   # or
   yarn install
   \`\`\`

2. Create a `.env.local` file in the root directory with:
   \`\`\`
   NEXT_PUBLIC_API_URL=http://localhost:8000
   \`\`\`

3. Start the development server:
   \`\`\`
   npm run dev
   # or
   yarn dev
   \`\`\`

The frontend will be running at http://localhost:3000

## Docker Setup (Optional)

You can also run the application using Docker:

### Backend

\`\`\`
cd backend
docker build -t fb-video-downloader-api .
docker run -p 8000:8000 fb-video-downloader-api
\`\`\`

## Usage

1. Open the application in your browser
2. Paste a Facebook video URL in the input field
3. Click "Process Video"
4. Select your preferred video quality
5. Click "Download Now" to download the video

## Legal Disclaimer

This tool is for personal use only. Please respect copyright laws and Facebook's terms of service when using this application.

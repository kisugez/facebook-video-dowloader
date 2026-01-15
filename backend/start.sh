#!/bin/bash
# Start script for the Facebook Video Downloader backend

echo "🚀 Starting Facebook Video Downloader Backend..."
echo ""

# Check if we're in the backend directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: Please run this script from the backend directory"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "⚠️  Virtual environment not found. Creating one..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null

# Install dependencies if needed
echo "📦 Checking dependencies..."
pip install -q -r requirements.txt

# Start the server
echo ""
echo "✅ Starting FastAPI server on http://localhost:8000"
echo "📚 API Documentation: http://localhost:8000/api/docs"
echo "🏥 Health Check: http://localhost:8000/health"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

python run.py

#!/bin/bash
# API Testing Script for Facebook Video Downloader
# This script demonstrates how to use the API endpoints

BASE_URL="http://localhost:8000"
API_URL="${BASE_URL}/api"

echo "🧪 Testing Facebook Video Downloader API"
echo "========================================"
echo ""

# Test 1: Health Check
echo "1️⃣  Testing Health Check Endpoint..."
echo "   GET ${BASE_URL}/health"
HEALTH_RESPONSE=$(curl -s "${BASE_URL}/health")
echo "   Response: ${HEALTH_RESPONSE}"
echo ""

# Test 2: Process Video (with example URL - will fail if not a real Facebook video)
echo "2️⃣  Testing Process Video Endpoint..."
echo "   POST ${API_URL}/process-video"
echo "   Body: {\"url\": \"https://www.facebook.com/watch?v=example\"}"
PROCESS_RESPONSE=$(curl -s -X POST "${API_URL}/process-video" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/watch?v=example"}')
echo "   Response: ${PROCESS_RESPONSE}"
echo ""

# Test 3: API Documentation
echo "3️⃣  API Documentation Available At:"
echo "   📚 Swagger UI: ${BASE_URL}/api/docs"
echo "   📖 ReDoc: ${BASE_URL}/api/redoc"
echo "   📝 OpenAPI Schema: ${API_URL}/openapi.json"
echo ""

# Test 4: Show expected request/response format
echo "4️⃣  Expected Request Format for /api/process-video:"
cat << 'EOF'
{
  "url": "https://www.facebook.com/watch?v=123456789"
}
EOF
echo ""

echo "5️⃣  Expected Response Format (Success):"
cat << 'EOF'
{
  "success": true,
  "message": "Video processed successfully",
  "download_id": "uuid-here",
  "thumbnail_url": "https://...",
  "title": "Video Title",
  "duration": 120,
  "formats": [
    {
      "format_id": "123",
      "resolution": "1280x720",
      "ext": "mp4",
      "filesize": 5000000,
      "format_note": "720p"
    }
  ]
}
EOF
echo ""

echo "6️⃣  Download Endpoint Usage:"
echo "   GET ${API_URL}/download/{download_id}?url=<encoded-url>&format_id=<format>"
echo ""

echo "✅ API Testing Complete!"
echo ""
echo "💡 Tips:"
echo "   - Use a real Facebook video URL to test the process-video endpoint"
echo "   - Visit ${BASE_URL}/api/docs for interactive API documentation"
echo "   - The download endpoint returns a file for download"

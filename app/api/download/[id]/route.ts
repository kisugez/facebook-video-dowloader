import { type NextRequest, NextResponse } from "next/server"

// This is a proxy endpoint to forward download requests to the FastAPI backend
export async function GET(request: NextRequest, { params }: { params: { id: string } }) {
  try {
    const id = params.id
    const url = new URL(request.url)
    const videoUrl = url.searchParams.get("url")
    const formatId = url.searchParams.get("format_id") || "best"

    if (!videoUrl) {
      return NextResponse.json({ error: "Video URL is required" }, { status: 400 })
    }

    // Forward the request to the FastAPI backend
    const apiUrl = process.env.API_URL || "http://localhost:8000"
    const response = await fetch(
      `${apiUrl}/api/download/${id}?url=${encodeURIComponent(videoUrl)}&format_id=${formatId}`,
      {
        headers: {
          "Content-Type": "application/json",
        },
      },
    )

    if (!response.ok) {
      const errorData = await response.json()
      return NextResponse.json({ error: errorData.message || "Failed to download video" }, { status: response.status })
    }

    // Stream the response back to the client
    const blob = await response.blob()
    return new NextResponse(blob, {
      headers: {
        "Content-Type": "application/octet-stream",
        "Content-Disposition": `attachment; filename="${id}.mp4"`,
      },
    })
  } catch (error) {
    console.error("Error downloading video:", error)
    return NextResponse.json({ error: "Failed to download video" }, { status: 500 })
  }
}

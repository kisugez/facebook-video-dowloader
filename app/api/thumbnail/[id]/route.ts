import { type NextRequest, NextResponse } from "next/server"

// This is a proxy endpoint to forward thumbnail requests to the FastAPI backend
export async function GET(request: NextRequest, { params }: { params: { id: string } }) {
  try {
    const id = params.id

    // Forward the request to the FastAPI backend
    const apiUrl = process.env.API_URL || "http://localhost:8000"
    const response = await fetch(`${apiUrl}/api/thumbnail/${id}`)

    if (!response.ok) {
      return NextResponse.json({ error: "Failed to fetch thumbnail" }, { status: response.status })
    }

    const data = await response.json()
    return NextResponse.json(data)
  } catch (error) {
    console.error("Error fetching thumbnail:", error)
    return NextResponse.json({ error: "Failed to fetch thumbnail" }, { status: 500 })
  }
}

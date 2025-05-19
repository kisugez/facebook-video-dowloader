"use server"

import { revalidatePath } from "next/cache"

// API URL - in production, this would be an environment variable
const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export async function downloadVideo(url: string) {
  try {
    // Call the FastAPI backend to process the video
    const response = await fetch(`${API_URL}/api/process-video`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      return {
        success: false,
        message: errorData.message || "Failed to process video",
      }
    }

    const data = await response.json()

    // Revalidate the path to ensure fresh data
    revalidatePath("/")

    return {
      success: true,
      downloadId: data.download_id,
      thumbnailUrl: data.thumbnail_url || `/api/thumbnail/${data.download_id}`,
      downloadUrl: `/api/download/${data.download_id}?url=${encodeURIComponent(url)}`,
      title: data.title,
      formats: data.formats,
      message: "Video processed successfully!",
    }
  } catch (error) {
    console.error("Error processing video:", error)
    return {
      success: false,
      message: "Failed to process video. Please try again.",
    }
  }
}

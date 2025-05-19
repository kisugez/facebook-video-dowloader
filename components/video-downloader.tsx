"use client"

import type React from "react"

import { useState } from "react"
import { downloadVideo } from "@/app/actions"
import { AlertCircle, Download, Loader2, Play, Check } from "lucide-react"
import Image from "next/image"

interface VideoFormat {
  format_id: string
  resolution: string
  ext: string
  filesize?: number
  format_note: string
}

export default function VideoDownloader() {
  const [url, setUrl] = useState("")
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle")
  const [message, setMessage] = useState("")
  const [downloadId, setDownloadId] = useState("")
  const [thumbnailUrl, setThumbnailUrl] = useState("")
  const [videoTitle, setVideoTitle] = useState("")
  const [formats, setFormats] = useState<VideoFormat[]>([])
  const [selectedFormat, setSelectedFormat] = useState("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!url.trim()) {
      setStatus("error")
      setMessage("Please enter a Facebook video URL")
      return
    }

    if (!url.includes("facebook.com") && !url.includes("fb.com")) {
      setStatus("error")
      setMessage("Please enter a valid Facebook video URL")
      return
    }

    setStatus("loading")
    setMessage("")
    setThumbnailUrl("")
    setFormats([])
    setSelectedFormat("")

    try {
      const result = await downloadVideo(url)

      if (result.success) {
        setStatus("success")
        setMessage("Video processed successfully!")
        setDownloadId(result.downloadId || "")
        setVideoTitle(result.title || "Facebook Video")

        if (result.thumbnailUrl) {
          setThumbnailUrl(result.thumbnailUrl)
        }

        if (result.formats && result.formats.length > 0) {
          setFormats(result.formats)
          setSelectedFormat(result.formats[0].format_id)
        }
      } else {
        setStatus("error")
        setMessage(result.message || "Failed to process video. Please try again.")
      }
    } catch (error) {
      setStatus("error")
      setMessage("An unexpected error occurred. Please try again.")
    }
  }

  const getDownloadUrl = () => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
    const formatParam = selectedFormat ? `&format_id=${selectedFormat}` : ""
    return `${apiUrl}/api/download/${downloadId}?url=${encodeURIComponent(url)}${formatParam}`
  }

  const formatFileSize = (bytes?: number) => {
    if (!bytes) return "Unknown size"
    const sizes = ["Bytes", "KB", "MB", "GB"]
    const i = Math.floor(Math.log(bytes) / Math.log(1024))
    return `${(bytes / Math.pow(1024, i)).toFixed(2)} ${sizes[i]}`
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="video-url" className="block text-sm font-medium text-gray-700 mb-1">
            Facebook Video URL
          </label>
          <input
            id="video-url"
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://www.facebook.com/watch?v=123456789"
            className="border border-gray-300 rounded-md px-4 py-2 w-full focus:outline-none focus:ring-2 focus:ring-[#1877F2] focus:border-transparent"
            disabled={status === "loading"}
          />
        </div>

        <button
          type="submit"
          className="bg-[#1877F2] hover:bg-[#166FE5] text-white font-medium py-2 px-4 rounded-md transition-colors w-full flex items-center justify-center"
          disabled={status === "loading"}
        >
          {status === "loading" ? (
            <>
              <Loader2 className="animate-spin mr-2 h-5 w-5" />
              Processing...
            </>
          ) : (
            <>
              <Download className="mr-2 h-5 w-5" />
              Process Video
            </>
          )}
        </button>
      </form>

      {status === "loading" && (
        <div className="mt-6 flex flex-col items-center justify-center">
          <div className="w-full h-48 bg-gray-100 rounded-md flex items-center justify-center">
            <Loader2 className="h-8 w-8 text-[#1877F2] animate-spin" />
          </div>
          <p className="text-sm text-gray-500 mt-2">Fetching video information...</p>
        </div>
      )}

      {status === "error" && (
        <div className="mt-4 p-3 bg-red-50 border border-red-200 rounded-md flex items-start">
          <AlertCircle className="h-5 w-5 text-red-500 mr-2 flex-shrink-0 mt-0.5" />
          <p className="text-red-700 text-sm">{message}</p>
        </div>
      )}

      {status === "success" && thumbnailUrl && (
        <div className="mt-6">
          <h3 className="text-lg font-medium text-gray-800 mb-2">{videoTitle}</h3>
          <div className="relative w-full aspect-video bg-black rounded-md overflow-hidden">
            <Image
              src={thumbnailUrl || "/placeholder.svg"}
              alt="Video thumbnail"
              fill
              className="object-cover"
              unoptimized={thumbnailUrl.startsWith("http")}
            />
            <div className="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center">
              <div className="h-16 w-16 rounded-full bg-[#1877F2] bg-opacity-80 flex items-center justify-center">
                <Play className="h-8 w-8 text-white ml-1" />
              </div>
            </div>
          </div>

          {formats.length > 0 && (
            <div className="mt-4">
              <h4 className="text-sm font-medium text-gray-700 mb-2">Select Quality:</h4>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {formats.map((format) => (
                  <div
                    key={format.format_id}
                    className={`border rounded-md p-2 cursor-pointer flex items-center ${
                      selectedFormat === format.format_id
                        ? "border-[#1877F2] bg-blue-50"
                        : "border-gray-200 hover:border-gray-300"
                    }`}
                    onClick={() => setSelectedFormat(format.format_id)}
                  >
                    <div className="flex-1">
                      <p className="font-medium text-sm">
                        {format.resolution} ({format.ext})
                      </p>
                      <p className="text-xs text-gray-500">
                        {format.format_note} {format.filesize ? `- ${formatFileSize(format.filesize)}` : ""}
                      </p>
                    </div>
                    {selectedFormat === format.format_id && <Check className="h-5 w-5 text-[#1877F2]" />}
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="mt-4">
            <a
              href={getDownloadUrl()}
              download={`${videoTitle}.mp4`}
              className="bg-[#1877F2] hover:bg-[#166FE5] text-white font-medium py-2 px-4 rounded-md transition-colors w-full flex items-center justify-center"
            >
              <Download className="mr-2 h-5 w-5" />
              Download Now
            </a>
          </div>
        </div>
      )}

      <div className="mt-6 text-center">
        <p className="text-xs text-gray-500">This tool is for personal use only. Please respect copyright laws.</p>
      </div>
    </div>
  )
}

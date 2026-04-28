import yt_dlp
import os

TEMP_DIR = "temp"

def download_video(url):
    print("⬇️ DOWNLOAD START")

    os.makedirs(TEMP_DIR, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{TEMP_DIR}/video.mp4",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("⬇️ DOWNLOAD DONE")

    return f"{TEMP_DIR}/video.mp4"


def split_chunks(video_path):
    print("✂️ CHUNK STEP")
    return [video_path]


def process_video(url):
    print("🔥 ENGINE START")

    video = download_video(url)
    chunks = split_chunks(video)

    print("🔥 ENGINE END")

    return {
        "file": chunks[0],
        "caption": "🔥 Epic Gameplay Moment",
        "hashtags": "#gaming #viral #shorts #fyp"
    }

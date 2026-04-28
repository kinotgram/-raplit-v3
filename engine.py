import yt_dlp
import os

TEMP_DIR = "temp"

def download_video(url):
    os.makedirs(TEMP_DIR, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{TEMP_DIR}/video.mp4",
        "format": "bestvideo+bestaudio"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"{TEMP_DIR}/video.mp4"


def split_chunks(video_path):
    # V3 SIMPLE VERSION: fake chunk system (30min placeholder)
    return [video_path]


def generate_caption():
    return "🔥 Best Gaming Moment Ever!"

def generate_hashtags():
    return "#gaming #viral #fyp #clips"


def process_video(url):
    video = download_video(url)

    chunks = split_chunks(video)

    # später: echte cutting engine
    first_chunk = chunks[0]

    return {
        "file": first_chunk,
        "caption": generate_caption(),
        "hashtags": generate_hashtags()
    }

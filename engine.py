import yt_dlp
import os

TEMP_DIR = "temp"

def download_video(url):
    print("STEP 1: download start")

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

    print("STEP 1 DONE")

    return f"{TEMP_DIR}/video.mp4"


def split_chunks(video_path):
    print("STEP 2: chunking")
    return [video_path]


def generate_caption():
    return "🔥 Epic Gameplay Moment"

def generate_hashtags():
    return "#gaming #viral #shorts #fyp"


def process_video(url):
    print("ENGINE START")

    video = download_video(url)

    chunks = split_chunks(video)

    print("ENGINE END")

    return {
        "file": chunks[0],
        "caption": generate_caption(),
        "hashtags": generate_hashtags()
    }

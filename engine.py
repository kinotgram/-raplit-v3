import yt_dlp
import os

TEMP_DIR = "temp"

def download_video(url):
    os.makedirs(TEMP_DIR, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{TEMP_DIR}/video.mp4",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"{TEMP_DIR}/video.mp4"


def split_chunks(video_path):
    # V3 simplified: 30min logic kommt später mit ffmpeg
    return [video_path]


def generate_caption():
    return "🔥 Epic Moment from Gameplay"

def generate_hashtags():
    return "#gaming #viral #shorts #fyp #clips"


def process_video(url):
    video = download_video(url)

    chunks = split_chunks(video)

    return {
        "file": chunks[0],
        "caption": generate_caption(),
        "hashtags": generate_hashtags()
    }

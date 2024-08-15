import yt_dlp
import os

import os
import urllib.request
import zipfile

import yt_dlp

def download_audio(video_url, output_path='downloads'):
    # yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


url="https://www.youtube.com/watch?v=RQ2nYUBVvqI"
if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_audio(video_url or url)

    

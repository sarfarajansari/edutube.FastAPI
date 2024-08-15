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
        'username': 'oauth2',
        'password': ''
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


url = "https://www.youtube.com/watch?v=RQ2nYUBVvqI"
if __name__ == '__main__':
    # video_url = input("Enter the YouTube video URL: ")
    # download_audio(video_url or url)

    import json
    import requests
    data = requests.post('https://tactiq-apps-prod.tactiq.io/transcript',
                         json={"langCode": "en", "videoUrl": "https://www.youtube.com/watch?v=RQ2nYUBVvqI"}, headers={
                             'accept':
                             '*/*',
                             'accept-encoding':
                             'gzip, deflate, br, zstd',
                             'accept-language':
                             'en-US,en;q=0.9',

                             'content-type':
                             'application/json',
                             'origin':
                             'https://tactiq.io',
                             'priority':
                             'u=1, i',
                             'referer':
                             'https://tactiq.io/',
                             'sec-ch-ua':
                             '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                             'sec-ch-ua-mobile':
                             '?0',
                             'sec-ch-ua-platform':
                             "Windows",
                             'sec-fetch-dest':
                             'empty',
                             'sec-fetch-mode':
                             'cors',
                             'sec-fetch-site':
                             'same-site',
                             'user-agent':
                             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
                         })

    print( data.text)

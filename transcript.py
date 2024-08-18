import requests
def get_transcript(videoId):
    data = requests.post('https://tactiq-apps-prod.tactiq.io/transcript',
                            json={"langCode": "en", "videoUrl": f"https://www.youtube.com/watch?v={videoId}"}, headers={
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

    return data.json()
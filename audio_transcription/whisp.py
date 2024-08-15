
import requests
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompt_values import ChatPromptValue
from openai import OpenAI
import os
import random
from dotenv import load_dotenv


load_dotenv()


def get_audio_file(id):
    params={
        'id': id,
        'cgeo': 'IN'
    }
    headers = {
        'x-rapidapi-key': "2eeb4478e6mshcf9866530ab966fp112115jsne49519e163ce",
        'x-rapidapi-host': "yt-api.p.rapidapi.com"
    }


    response = requests.get('https://yt-api.p.rapidapi.com/dl', params=params, headers=headers)

    if response.status_code != 200:
        return None
    
    data = response.json()

    formats = data.get('adaptiveFormats')

    if not formats:
        return None


    audios = []


    for format in formats:
        if "audio" in format.get('mimeType'):
            if format.get('audioQuality') == 'AUDIO_QUALITY_MEDIUM':
                audios.insert(0, format.get('url'))

            else:
                audios.append(format.get('url'))

    
    if len(audios) == 0:
        return None
    
    return audios[0]
    
    

def download_audio(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
        file.close()


def transcribe_audio(file_url):
    file_path = f"audio{random.randint(0,100)}.mp3"
    download_audio(file_url, file_path)
    client = OpenAI()
    
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format='verbose_json'
        )
        audio_file.close()
      
    os.remove(file_path)
    return transcription







def get_transcript(videoId):
    audi_file = get_audio_file(videoId)

    if not audi_file:
        raise Exception("Audio file not found")
    
    segments = transcribe_audio(audi_file).segments
    segments = [(round(segment.get('start'),1),round(segment.get('end'),1),segment.get('text')) for segment in segments if segment.get('text')]

    return  segments
    


    

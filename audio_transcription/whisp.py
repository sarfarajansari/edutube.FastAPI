
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


    audioList = []

    


    for format in reversed(formats):
        if "audio" in format.get('mimeType'):
            if format.get('audioQuality') == 'AUDIO_QUALITY_LOW':
                audioList.insert(0, format.get('url'))
                break

            else:
                audioList.append(format.get('url'))
    if len(audioList) == 0:
        return None
    
    
    return audioList
    
    

APP_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwiDf5z0iyNYpj_UGw6f6ImdgsC5E7iN_CAy1Ox_I3XZ4pwHW8P8I-t5dpQtsiycO_b9w/exec'


def save_base64_to_file(base64_string, file_path):
    print('saving base64 to file')
    import base64
    try:
        # Decode the Base64 string
        file_data = base64.b64decode(base64_string)
        
        # Write the decoded data to a file
        with open(file_path, 'wb') as file:
            file.write(file_data)
        
        print(f"File saved successfully as: {file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def download_audio(audioList, save_path):


    for url in audioList:
        print(url)
        try:
            response = requests.post(APP_SCRIPT_URL,json={
            'url': url
            },timeout=3000)

            print('file received')
            print(response.status_code)
            data = response.text
            save_base64_to_file(data, save_path)
            break
        except Exception as e:
            print(e)
            continue
    # with open(save_path, 'wb') as file:
    #     file.write(response.content)
    #     file.close()
 

def transcribe_audio(audioList):
    file_path = f"audio{random.randint(0,100)}.mp3"
    download_audio(audioList, file_path)
    print('audio downloaded')
    client = OpenAI()

    print('transcribing audio')
    
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format='verbose_json'
        )
        audio_file.close()

    print('audio transcripted')
      
    os.remove(file_path)

    print('audio deleted')
    return transcription







def get_transcript(videoId):
    audioList = get_audio_file(videoId)

    print('audio url created')

    if not audioList:
        raise Exception("Audio file not found")
    
    segments = transcribe_audio(audioList).segments
    segments = [(round(segment.get('start'),1),round(segment.get('end'),1),segment.get('text')) for segment in segments if segment.get('text')]

    return  segments
    


    

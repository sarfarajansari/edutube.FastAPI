from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile
from moviepy.editor import VideoFileClip
from openai import OpenAI
from random import randint

# with open(file.filename, "wb") as buffer:
#         buffer.write(await file.read())
    
#     # Convert video to audio
#     video = VideoFileClip(file.filename)
#     audio = video.audio
#     audio_filename = f"audio_{file.filename}.mp3"
#     audio.write_audiofile(audio_filename)
    
#     # Close the clips
#     audio.close()
#     video.close()
    
#     # Remove the temporary video file
#     os.remove(file.filename)


def extract_audio(filepath):

    video = VideoFileClip(filepath)
    audio = video.audio
    randomeFile= f'temp/{randint(0,10000)}.mp3'
    audio.write_audiofile(randomeFile)

    audio.close()
    video.close()
    return randomeFile


def transcribe(file_path):
    client = OpenAI()

    print(file_path)
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format='verbose_json'
        )
        audio_file.close()

        segments =transcription.segments
        segments = [(round(segment.get('start'),1),round(segment.get('end'),1),segment.get('text')) for segment in segments if segment.get('text')]

        return segments

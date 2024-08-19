from pydub import AudioSegment
import os

def split_audio(input_file, chunk_length_minutes=5):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the length of each chunk in milliseconds
    chunk_length_ms = chunk_length_minutes * 60 * 1000

    # Directory to save chunks
    output_directory = "temp"
    os.makedirs(output_directory, exist_ok=True)

    # Split audio into chunks
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    # List to store filenames of chunks
    chunk_filenames = []

    # Save chunks to files and collect filenames
    file_format = input_file.split('.')[-1]  # Preserve original file format
    for i, chunk in enumerate(chunks):
        chunk_file = os.path.join(output_directory, f"chunk_{i + 1}.{file_format}")
        chunk.export(chunk_file, format=file_format)
        chunk_filenames.append(chunk_file)
        print(f"Saved chunk {i + 1} as {chunk_file}")

    return chunk_filenames
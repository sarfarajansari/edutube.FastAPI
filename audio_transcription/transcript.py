import tactiq
import whisp

def get_transcript(videoId):
    method = int(input("Enter the method to use: "))

    if method == 1:
        return tactiq.get_transcript(videoId)
    
    elif method == 2:
        return whisp.get_transcript(videoId)
    


if __name__ == '__main__':
    videoId =   input("video id")  or "RQ2nYUBVvqI"
    print(get_transcript(videoId))


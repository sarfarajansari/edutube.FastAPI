
import json
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from promptTemplate import topic_search_prompt
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_URL = "https://www.googleapis.com/youtube/v3/"


def fetch_youtube_video(inputData) -> dict[str, str]:
    search_query = inputData["search_query"]
    max_results = inputData["max_results"]
    print("page number", inputData.get("pageNumber"))

    api_key = os.getenv("YT_API_KEY")

    print("API KEY", api_key)

    url = f"{API_URL}search?part=snippet&type=video&maxResults={max_results}&q={search_query}&key={api_key}&order=viewCount&regionCode=IN"

    if inputData.get("nextPageToken"):
        url += f"&pageToken={inputData.get('nextPageToken')}"

    data = requests.get(url).json()
    result = inputData.get("result") or []


    videoItems = data.get("items") or []

    for item in videoItems:
        if item["id"].get("videoId"):
            try:
                transcript = str(YouTubeTranscriptApi.get_transcript(
                    item["id"].get("videoId")))
                

                if transcript:
                    result.append({
                        "title": item["snippet"]["title"],
                        "description": item["snippet"]["description"],
                        "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                        "videoId": item["id"].get("videoId"),
                        "transcript": transcript,
                    })
            except Exception as e:
                print("Transcript not found", item["id"].get("videoId"))
                continue


        if len(result)> max_results:
            break

    if len(result) == 0:
        inputData["nextPageToken"] = data.get("nextPageToken")
        inputData["pageNumber"] = (inputData.get("pageNumber")or 0 ) + 1
        inputData["result"] = result
        return fetch_youtube_video(inputData)
    
    data["videos"] = result

    return {
        "nextPageToken": data.get("nextPageToken"),
        "videos": result
    }


def generateVideos(search_query: str, max_results: int = 1,nextPageToken:str=None,attempt=0) -> list[dict[str, str]]:
    data = fetch_youtube_video(
        {"search_query": f"Educational video on {search_query}", "max_results": max_results,"nextPageToken": nextPageToken,"pageNumber":1})
    llm = ChatOpenAI(temperature=0.2, model="gpt-4o")


    chain = topic_search_prompt | llm | StrOutputParser()

    print("Number of videos with transcript", len(data['videos']))
    result = []
    for item in data["videos"]:
        res = chain.invoke({"topic": search_query, "transcript": item['transcript']}).replace(
            '```json\n', '').replace('```', '')

        try:
            item['concept'] = json.loads(res)
            if len(item['concept']) == 0:
                continue
            item['topic'] = search_query
            result.append(item)
        except:
            pass

    if len(result) >= 0:
        return {
            "nextPageToken": data.get("nextPageToken"),
            "videos": result
        }
    
    if attempt < 3:
        return generateVideos(search_query, max_results, nextPageToken,attempt+1)
    return None

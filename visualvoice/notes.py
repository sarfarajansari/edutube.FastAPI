from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt_content_idea = ChatPromptTemplate.from_messages([
        ("system", """
You will be given transcripts of an educational video. Your task is to create concise notes on the video content.
You need to return as array of note cards {format}. To create a note text, you need to consider a set of transcribed sentences and make a explanation in better words,expanding the idea.
You can make a maximum of 2 notes. Every note should have some important fundamental concept of the video and important educational point, you need to explain that point properly.
The output should be strictly JSON format.
"""),

        ("user",
         "transcript {transcript}"),
])


def get_notes(transcript):
    llm = ChatOpenAI(temperature=0.7, model="gpt-4o")

    output_parser = StrOutputParser()

    chain = prompt_content_idea | llm | output_parser

    return chain.invoke({"transcript": transcript,'format':'[{startTime, note}]'}).replace('```json\n', '').replace('```', '')
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from promptTemplate import prompt_content_idea, prompt_content_generation

from dotenv import load_dotenv
load_dotenv()


def generateHtmlContent(topic):
    llm = ChatOpenAI(temperature=0.4, model="gpt-4o")

    output_parser = StrOutputParser()

    chain = prompt_content_idea | llm | output_parser | prompt_content_generation | llm | output_parser

    return chain.invoke({"topic": topic}).replace('```html\n', '').replace('```', '')


if __name__ == "__main__":
    topic = input("Enter the topic: ")
    html_content = generateHtmlContent(topic=topic)

    open("index.html", "w").write(html_content)

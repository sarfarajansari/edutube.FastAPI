from langchain_core.prompts import ChatPromptTemplate

prompt_content_idea = ChatPromptTemplate.from_messages([
        ("system", """
I want you to generate prompt for a coder Agent.
The agent will take the prompt to write html,css,js interactive educational content.
You need to help the coder agent design the content based on the topic given by the user.
eg: if the user gives the topic laws of motion, you need to give strict and specific instructuions to the coder agent,
like Create a html page with a ball and a wall. The ball should move in a straight line and bounce back when it hits the wall, etc. Avoid images in HTML, output should have maximum 800 characters."""),

        ("user",
         "Generate a prompt for a coder agent to write html css js interactive educational content on the topic of {topic}"),
])



HTML_TEMPLATE =open("template.html").read()
def prompt_content_generation(input_data):
    print("Generating html with LLM input")
    return ChatPromptTemplate.from_messages([
            ("system", "You are a web developer with experience in animation, good design. You are tasked with creating an educational content on the instructions given by user.Output should only include HTML,CSS, JS. No additinal text/explantion is required"),
            ("system", r"""You need to use this boiler plate code to start with, make use of the header for the title, keep header at top: {html}"""),
            ("user", "{input_data}")]).invoke({"input_data": input_data, "html": HTML_TEMPLATE})



topic_search_prompt = ChatPromptTemplate.from_messages([
        ("system", """
User will be giving a YT video transcript and a topic or query, you need to do the following:
You need find distinguish important concepts related to the topic at different timestamps (start and end time) in the transcript. 
By important I mean something that is part of a field of study, like important formulas, and theory, etc. 
and return an Array of objects with the following structure:
         start:start time,
         end : end time,
         concept description: in short, 

Each object should have different concepts, if you don't find any, return empty array, Output should be strictly JSON.
         The maximum length of array should be 3.
         """),


        ("user","topic : {topic}, transcript {transcript}"),
])

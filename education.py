import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def remove_education(paragraph):
        
    content = "Remove anything related to the following words: education, school, degrees, diplomas, graduates, graduation, credentials, academics, credits, credit, credit substitutions, courses, classes, and so on."
    content = content + "\n" + paragraph

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )

    pure_skill_set = chat_completion.choices[0].message.content

    return pure_skill_set

import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def remove_repetition(paragraph):
    
    content = "Remove repetitive information from the following paragraph."
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

    less_repetitive_paragraph = chat_completion.choices[0].message.content

    return less_repetitive_paragraph
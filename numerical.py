import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def remove_numbers(paragraph):
    
    content = "Remove anything related to the these words: years, number of years, months, number of months, 3+ years, 4+ months, 1 year experience, 2 year exp., and so on. No numbers should appear in your response."
    content = content + paragraph

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )

    number_free_paragraph = chat_completion.choices[0].message.content

    return number_free_paragraph
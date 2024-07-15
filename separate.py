import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def separate_skills(paragraph):

    content = "Separate each specific skill by \n. When in doubt, separate similar items instead of grouping together as one item."
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

    separated_skills = chat_completion.choices[0].message.content

    return separated_skills
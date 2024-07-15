import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def group_skills(summarized_skill_set):

    content = "Rewrite the paragraph such that skills are grouped by similarity."
    content = content + "\n" + summarized_skill_set

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )

    group_skill_set = chat_completion.choices[0].message.content

    return group_skill_set

import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def summarize_skills(posting):

    required_skills = posting['minimum_qual_requirements']
    content = "In one paragraph, concisely summarize what skills are required for this job. Omit educational and degree information."
    content = content + "\n" + required_skills

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )

    skills = chat_completion.choices[0].message.content

    return skills
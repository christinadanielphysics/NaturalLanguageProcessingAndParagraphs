import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_cleaned_skill(uncleaned_skill):

    content = "Remove any newline characters from the following requirement. Remove right-trailing periods."
    content = content + "\n" + uncleaned_skill

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )

    cleaned_skill = chat_completion.choices[0].message.content
    return cleaned_skill

def clean_skills(condensed_skill_set):

    cleaned_skill_set = []
    for condensed_skill in condensed_skill_set:
        cleaned_skill = get_cleaned_skill(condensed_skill)
        cleaned_skill_set.append(cleaned_skill)

    return cleaned_skill_set
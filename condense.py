import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_condensed_skill(verbose_skill):

    content = "In 1-3 words, concisely describe the following job requirement."
    content = content + "\n" + verbose_skill

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )

    condensed_skill = chat_completion.choices[0].message.content
    return condensed_skill


def condense_skills(verbose_skill_set):

    condensed_skill_set = []
    for verbose_skill in verbose_skill_set:
        condensed_skill = get_condensed_skill(verbose_skill)
        condensed_skill_set.append(condensed_skill)

    return condensed_skill_set
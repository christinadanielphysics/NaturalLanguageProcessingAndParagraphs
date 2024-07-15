import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()  # take environment variables from .env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def remove_generic(paragraph):

    content = "Remove requirements characterized by vague or generic words and phrases such as required, minimum experience, relevant experience, related work experience, previous experience, experience required, education and experience substitutions, equivalent qualifications accepted, probation period, probationary period, probationary, education/experience equivalent, and so on."
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

    specific_skill_set = chat_completion.choices[0].message.content
    
    return specific_skill_set

    


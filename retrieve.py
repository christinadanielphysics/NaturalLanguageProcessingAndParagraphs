import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json

def retrieve_data():
    url = "https://extractjobpostingsdata-gmtumocfua-uc.a.run.app/get_data"
    response = requests.get(url)
    data = response.json()
    return data
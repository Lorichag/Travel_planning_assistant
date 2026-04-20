from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv(override=True)

groq_api_key = os.getenv('GROQ_API_KEY')
groq_base_url = os.getenv('GROQ_BASE_URL')

client = OpenAI(
    api_key=groq_api_key,
    base_url=groq_base_url
)
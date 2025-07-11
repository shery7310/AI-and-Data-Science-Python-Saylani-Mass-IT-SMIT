from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key= GOOGLE_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

question = "What is 2 * 5 ?"
message = [{"role": "system", "content": "You are a math agent and gives answers only in numbers"},
           {"role": "user", "content": question}]

response = client.chat.completions.create(
    model="gemini-2.0-flash-lite",
    messages = message
)


print(response.choices[0].message.content)

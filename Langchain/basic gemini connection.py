from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv("gemini"):
    api_key = os.getenv("gemini")
else:
    api_key = input("Enter Your Api Key here, our put required api key in .env file")

# Initialize the Gemini model object
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("gemini")
) # this is abstracting many things that we usually need to connect with other LLMs

# Send a simple query
query = "Why is Langchain better than openai agents sdk? Explain briefly"
response = llm.invoke(query)

print("Response:", response.content)

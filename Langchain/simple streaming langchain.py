import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("gemini")

model_name = os.getenv("gemini-2.5-flash")

def stream_from_gemini(query: str):
    llm = ChatGoogleGenerativeAI(model= model_name, streaming=True, google_api_key = api_key)
    response = llm.stream(["system", "You are a helpful assistant that answers appropriately",
                                      "human", query])
    for chunk in response:
        yield chunk.content

user_query = input("Enter Your Query:\n")

for chunk in stream_from_gemini(user_query):
    # print(chunk, end="", flush=True)
    print(chunk)
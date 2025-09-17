import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
api_key = os.getenv("gemini")

model_name = os.getenv("gemini-2.5-flash")

def stream_from_gemini(query: str, prompt_template: ChatPromptTemplate):
    llm = ChatGoogleGenerativeAI(model= model_name, streaming=True, google_api_key = api_key)
    chain = prompt_template | llm
    response = chain.stream({"input": query})
    for chunk in response:
        yield chunk.content

def non_stream(query: str, prompt_template: ChatPromptTemplate):
    llm = ChatGoogleGenerativeAI(model=model_name, streaming=False, google_api_key=api_key)
    chain = prompt_template | llm
    response = chain.invoke({"input": query})
    return response.content


# prompt = ChatPromptTemplate.from_messages([
#         (
#             "system",
#             "You are a helpful assistant that answer's appropriately",
#         ),
#         ("human", "{query}"),
#     ]
# )

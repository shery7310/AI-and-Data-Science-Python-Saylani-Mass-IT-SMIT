from fastapi import APIRouter
from fastapi.responses import StreamingResponse, Response, JSONResponse
from agents import stream_from_gemini, non_stream # my own functions
from langchain_core.prompts import ChatPromptTemplate

router = APIRouter()

@router.get("/stream_answer")
async def stream_answer(query: str):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant that answer's appropriately",
        ),
        ("human", "{input}"),
    ]
    )
    response = StreamingResponse(stream_from_gemini(query, prompt), media_type="text/plain")
    return response

@router.get("/non_stream_answer")
async def non_stream_answer(query: str):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant that answer's appropriately",
        ),
        ("human", f"{query}"),
    ]
    )
    response = Response(non_stream(query, prompt), media_type="text/plain")
    return response

"""
Example Prompt
prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant that answer's appropriately",
        ),
        ("human", "{input}"),
    ]
)

Sample Endpoint for Non Streaming: 
http://127.0.0.1:8000/non_stream_answer?query=What%20is%20python%20language
Sample Endpoint for Streaming:
http://127.0.0.1:8000/stream_answer?query=What%20is%20python%20language
"""

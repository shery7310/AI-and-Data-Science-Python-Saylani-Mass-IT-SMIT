import asyncio
from openai import OpenAI
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('gemini')

gemini_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini_model = "gemini-2.5-flash"

external_client = AsyncOpenAI(api_key=api_key, timeout=300.0, base_url=gemini_base_url)

model = OpenAIChatCompletionsModel(model= gemini_model, openai_client= external_client)

config = RunConfig(model = model, tracing_disabled = True, model_provider = external_client)

async def stream_gemini():
    stream = await external_client.chat.completions.create(
        model= gemini_model,
        messages=[
            {"role": "system", "content": "You are a math assitant."},
            {"role": "user", "content": "Solve this quadratic equation step wise x^2 - 3x - 4 = 0"}
        ],
        stream=True,
    )

    async for event in stream:
        if event.choices[0].delta.content is not None:
            print(event.choices[0].delta.content, end="", flush=True)

asyncio.run(stream_gemini())

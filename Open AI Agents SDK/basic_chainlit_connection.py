import chainlit as cl
import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, RunConfig, Agent, Runner
from dataclasses import dataclass


@dataclass()
class AppConfig:
    load_dotenv()
    timeout: int = 300
    api_key: str = os.getenv('gemini')
    base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai/",
    provider_model: str =  "gemini-2.5-flash"

client_config = AppConfig()

external_client = AsyncOpenAI(api_key = client_config.api_key,
                                  timeout = client_config.timeout,
                                  base_url = client_config.base_url[0])

model = OpenAIChatCompletionsModel(model = client_config.provider_model,
                                       openai_client = external_client)

config = RunConfig(model=model, tracing_disabled=True, model_provider = external_client)


agent = Agent(name="Assistant", instructions="You are a helpful assistant", model = model)

@cl.on_message
async def handle_msg(message: cl.Message):
    result = await Runner.run(agent, input = message.content, run_config = config )
    print(result.final_output)
    await cl.Message(content=f"{result.final_output}").send()


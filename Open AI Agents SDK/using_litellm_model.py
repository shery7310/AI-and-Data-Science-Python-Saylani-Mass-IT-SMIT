from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
Model = "gemini/gemini-2.5-flash"
gemini_api_key = os.getenv("gemini")


async def main(model: str, api_key: str):
    agent = Agent(
        name="Assistant",
        instructions="You respond clearly as you're a helpful agent.",
        model= LitellmModel (model=model, api_key=api_key)
    )

    result = await Runner.run(agent, "What is 2 * 9?")
    print(result.final_output)

asyncio.run(main(Model, gemini_api_key))
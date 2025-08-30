import asyncio
import requests
from datetime import datetime
from agents import Agent, WebSearchTool, function_tool, OpenAIChatCompletionsModel, Runner, RunConfig
from openai import AsyncOpenAI
from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass()
class AppConfig:
    load_dotenv()
    timeout: int = 300
    api_key: str = os.getenv('gemini')
    base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai/",
    provider_model: str =  "gemini-2.5-flash"

client_config = AppConfig()

@function_tool()
def get_date_time():
    current_date_time = datetime.now()
    return current_date_time.isoformat()

@function_tool()
def brave_web_search(query, count=5):
    brave_api_key = os.getenv('brave_key')
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {"Accept": "application/json", "X-Subscription-Token": brave_api_key}
    params = {"q": query, "count": count}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for item in data.get("web", {}).get("results", []):
        results.append({"title": item["title"], "url": item["url"]})

    return results

@function_tool()
def get_user_details():
    user_name = input("Enter your Name")
    user_age = input("Enter your Age")
    user_career = input("Enter your Profession")
    return user_name, user_age, user_career

user_input = [{"role": "user", "content": "Search Web for Learn OpenAI Agents SDK"}]


async def llm_result():

    external_client = AsyncOpenAI(api_key = client_config.api_key, timeout = client_config.timeout,
                                  base_url = client_config.base_url[0])

    model = OpenAIChatCompletionsModel(model = client_config.provider_model, openai_client = external_client)

    config = RunConfig(model = model, tracing_disabled = True, model_provider = external_client)

    agent = Agent("assistant", "You are a helper assistant, be kind.", model = model, tools = [get_date_time, get_user_details, brave_web_search])

    result = await Runner.run(agent, user_input, run_config = config)

    return result.final_output

print(asyncio.run(llm_result()))



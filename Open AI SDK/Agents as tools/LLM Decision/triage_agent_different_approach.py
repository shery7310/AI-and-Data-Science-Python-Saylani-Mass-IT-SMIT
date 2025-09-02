
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, function_tool
import json
from dotenv import load_dotenv
import datetime
import os
from openai import AsyncOpenAI
load_dotenv()
from pydantic import BaseModel
from typing import List
import asyncio

class Output_Gen(BaseModel):
    timings: List[str]


load_dotenv()
api_key=os.getenv('gemini')
gemini_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini_model = "gemini-2.5-flash"

external_client = AsyncOpenAI(api_key=api_key, timeout=300.0, base_url=gemini_base_url)

model = OpenAIChatCompletionsModel(model= gemini_model, openai_client= external_client)

config = RunConfig(model = model, tracing_disabled = True, model_provider = external_client)

@function_tool()
def current_month():
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
              5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
              10: 'October', 11: 'November', 12: 'December'}
    return months[datetime.date.today().month] # August

@function_tool()
def get_peak_hours(city: str, month):
    if city.lower() == "lahore" or city.lower() == "lhr":
        lhr_data = json.load(open('lahore_peak_timings.json'))
        return lhr_data
    elif city.lower() == "fsd" or city.lower() == "faisalabad":
        fsd_data = json.load(open('faisalabad_peak_timings.json'))
        return fsd_data
    else:
        return False

fsd_agent = Agent(name = "Faisalabad Agent", instructions = "You are an agent for Faisalabad related queries if"
                                                        "a customers asks for peak hours from any time"
                                                        "you first check the current month and then you fetch "
                                                        "peak hours for that month, if user provides month himself"
                                                        "then give him peak hours for that month for faisalad",
                         model = model,
                         tools = [current_month, get_peak_hours],
                         handoff_description = "For Faisalabad or Fsd related peak hours queries")



lhr_agent = Agent(name = "Lahore Agent", instructions = "You are an agent for Lahore related queries if"
                                                        "a customers asks for peak hours from any time"
                                                        "you first check the current month and then you fetch "
                                                        "peak hours for that month"
                                                        "if user provides month himself"
                                                        "then give him peak hours for that month for lhr",
                         model = model,
                         tools = [current_month, get_peak_hours],
                         handoff_description = "For Lahore or Lhr related peak hours queries")

orchestrating_tool = Agent(name = "Orchestrator", instructions = "You will decide which agent to call for a task",
                           model = model,
                           handoffs = [lhr_agent, fsd_agent])

# query = input("Which City are you from?\n").lower()
# query = f"I am from {query} what are my current peak hours?"

async def ask_user():
    query2 = "I am from lhr what are peak hours for current month?"
    query3 = "I am from Faisalabad the peak hours 7 PM to 11 PM are for which months? "
    result = await Runner.run(orchestrating_tool, query2, run_config = config)
    return result.final_output

print(asyncio.run(ask_user()))
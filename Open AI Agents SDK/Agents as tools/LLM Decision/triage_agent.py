
from agents import Agent, Runner, set_tracing_disabled
from agents.tool import function_tool
from agents.extensions.models.litellm_model import LitellmModel
import json
from dotenv import load_dotenv
import datetime
import os
load_dotenv()


Model = "gemini/gemini-2.5-flash"
gemini_api_key = os.getenv("gemini")

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
                         model = LitellmModel(model= Model, api_key= gemini_api_key),
                         tools = [current_month, get_peak_hours],
                         handoff_description = "For Faisalabad or Fsd related peak hours queries")



lhr_agent = Agent(name = "Lahore Agent", instructions = "You are an agent for Lahore related queries if"
                                                        "a customers asks for peak hours from any time"
                                                        "you first check the current month and then you fetch "
                                                        "peak hours for that month"
                                                        "if user provides month himself"
                                                        "then give him peak hours for that month for lhr",
                         model = LitellmModel(model= Model, api_key= gemini_api_key),
                         tools = [current_month, get_peak_hours],
                         handoff_description = "For Lahore or Lhr related peak hours queries")


orchestrating_tool = Agent(name = "Orchestrator", instructions = "You will decide which agent to call for a task",
                           model = LitellmModel(model= Model, api_key= gemini_api_key),
                           handoffs = [lhr_agent, fsd_agent])

# query = input("Which City are you from?\n").lower()
# query = f"I am from {query} what are my current peak hours?"

query2 = "I am from Faisalabad what are peak hours for January?"
result = Runner.run_sync(orchestrating_tool, query2)
print(result.final_output)

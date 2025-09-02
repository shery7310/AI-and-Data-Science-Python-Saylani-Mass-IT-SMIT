import os
from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAI
from agents import OpenAIChatCompletionsModel, RunConfig, Agent, Runner
import asyncio
from pydantic import BaseModel
from typing import List

load_dotenv()
api_key=os.getenv('gemini')

gemini_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini_model = "gemini-2.5-flash"


external_client = AsyncOpenAI(api_key=api_key, timeout=300.0, base_url=gemini_base_url)

model = OpenAIChatCompletionsModel(model= gemini_model, openai_client= external_client)

config = RunConfig(model = model, tracing_disabled = True, model_provider = external_client)


from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)

class Wrong_words(BaseModel):
    used: bool
    explanation: str

offensive_words_guardrail = Agent(name="Offensive Words Guardrail Agent",
                                instructions="You will try to stop user from using offensive words such as fuck|bad|wrong",
                                model = model,
                                output_type = Wrong_words)

@input_guardrail()
async def cheat_detection_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]):
    detection_ans = await Runner.run(offensive_words_guardrail, input)
    print(detection_ans)
    print()
    return GuardrailFunctionOutput(tripwire_triggered=detection_ans.final_output.used,
                                   output_info=detection_ans.final_output)

greet_agent = Agent(name="greet agent",
              instructions="You will greet the user with good greetings",
              model = model,
              input_guardrails=[cheat_detection_guardrail])

try:
    response = Runner.run_sync(greet_agent, "Hi Fuck You!")
    print("Guardrail didn't trigger")
    print("Response: ", response.final_output)

except InputGuardrailTripwireTriggered as e:
    print("Homework cheat guardrail triggered")
    print("Exception details:", str(e))

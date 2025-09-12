import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)
import time

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("gemini")
gemini_judge = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

messages = [{'role': 'user',
  'content': """"Create a difficult reasoning question for to judge LLMs and their outputs,
             keep question short, only ask question don't provide reason why you asked a question,
             Now respond this way do not include markdown format"""}]

response = gemini_judge.chat.completions.create(model="gemma-3-27b-it", messages= messages)

question = f"""{response.choices[0].message.content}"""


model_to_use = ["gemma-3-12b-it", "gemini-2.0-flash-thinking-exp-1219",
                "gemini-2.0-flash-thinking-exp", "gemini-2.0-flash-thinking-exp-01-21"]

LLM1 = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

LLM2 = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

LLM3 = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

LLM4 = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

messages = [{'role': 'user',
  'content': f"""Answer this question: {question}"""}]

LLM1_response = LLM1.chat.completions.create(model= model_to_use[0], messages= messages)

time.sleep(5)

LLM2_response = LLM2.chat.completions.create(model= model_to_use[1], messages= messages)

time.sleep(5)

LLM3_response = LLM3.chat.completions.create(model= model_to_use[2], messages= messages)

time.sleep(5)

LLM4_response = LLM4.chat.completions.create(model= model_to_use[3], messages= messages)

time.sleep(5)

llm_responses = {model_to_use[0]: LLM1_response.choices[0].message.content,
                 model_to_use[1]: LLM2_response.choices[0].message.content,
                 model_to_use[2]: LLM3_response.choices[0].message.content,
                 model_to_use[3]: LLM4_response.choices[0].message.content}

messages = [{'role': 'user',
  'content': f"""Which LLM answered this question that you asked best?, this is the question: {question},
              {model_to_use[0]} answered this: {llm_responses[model_to_use[0]]},
              {model_to_use[1]} answered this: {llm_responses[model_to_use[1]]},
              {model_to_use[2]} answered this: {llm_responses[model_to_use[2]]},
              {model_to_use[3]} answered this: {llm_responses[model_to_use[3]]}
              """}]

time.sleep(5)

decision_response = gemini_judge.chat.completions.create(model="gemma-3-27b-it", messages= messages)

print(decision_response.choices[0].message.content)
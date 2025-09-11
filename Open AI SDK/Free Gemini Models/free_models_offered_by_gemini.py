from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
  api_key= os.getenv('gemini'),
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

free_models = []
models = client.models.list()
for model in models:
    if "pro" not in model.id:
        free_models.append(model.id.strip('models/'))

print(free_models[0:11])
print(free_models[11:21])
print(free_models[21:31])
print(free_models[31:41])
print(free_models[41:57])
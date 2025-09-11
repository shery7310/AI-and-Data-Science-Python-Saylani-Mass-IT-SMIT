### openai = OpenAI()

#### For connecting to HTTP endpoints 

We are creating an instance of OpenAI() class, it is a lightweight library for connecting to openai's endpoints on the cloud. Call it a client library, it's a wrapper library around endpoints, that calls HTTP endpoints. 

#### Connecting to HTTP endpoints 

```python

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

google_api_key = api_key
gemini_client = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

response = gemini_client.chat.completions.create(model="gemini-2.5-flash", messages=[{"role":"user", "content": "what is 2+2?"}])

print(response.choices[0].message.content)

```

See that we are passing base_url, api_key to OpenAI which in turn is returning a client that we are storing in gemini_client variable. This client help us communicate using api key in our case we are using gemini's key.

The in the next line we are using `chat.completions.create` with the client we created i.e. `gemini_client`. We are passing the chat completions api as it's called our client, name of model and the message we want to send.
#### Conversing with LLMs

We usually converse with LLMs using this format:

```python
messages = {{"role": "user", "content", "What is 2+2?"}}
```

We've seen even LLMs internally saving data like this. 
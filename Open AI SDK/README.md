To run basic_chainlit_connection.py file:

First Run:

<pre>
uv add chainlit dotenv openai openai-agents
</pre>

Then run `uv run chainlit run basic_chainlit_connection.py -w`, it will load the app on: `http://localhost:8000/`

To use LitellmModel (using_litellm_model.py) you need to add:

<pre>
uv add openai-agents[litellm]
</pre>

Reference: 
https://openai.github.io/openai-agents-python/models/litellm/ 

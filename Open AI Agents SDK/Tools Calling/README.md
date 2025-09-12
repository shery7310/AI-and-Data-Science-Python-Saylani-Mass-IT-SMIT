### Tools

Tools let agents take actions: things like fetching data, running code, 
calling external APIs, and even using a computer. 
There are three classes of tools in the Agent SDK:

- Hosted tools: these run on LLM servers alongside the AI models. 
  OpenAI offers retrieval, web search and computer use as hosted tools.
- Function calling: these allow you to use any Python function as a tool. 
- Agents as tools: this allows you to use an agent as a tool, 
  allowing Agents to call other agents without handing off to them.

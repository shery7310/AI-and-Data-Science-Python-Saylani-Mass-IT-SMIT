import chainlit as cl
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, RunConfig, Agent, Runner
from connection_class import AppConfig as client_config # My own class
from openai.types.responses import ResponseTextDeltaEvent

external_client = AsyncOpenAI(api_key = client_config.api_key,
                                  timeout = client_config.timeout,
                                  base_url = client_config.base_url[0])

model = OpenAIChatCompletionsModel(model = client_config.provider_model,
                                       openai_client = external_client)

config = RunConfig(model=model, tracing_disabled=True, model_provider = external_client)


agent = Agent(name="Assistant", instructions="You are a helpful assistant", model = model)

@cl.on_chat_start
async def chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content=f"Hi Welcome To Your Own Agent").send()

@cl.on_message
async def handle_msg(message: cl.Message):
    history = cl.user_session.get("history")

    msg = cl.Message(content="")
    await msg.send()

    history.append({"role": "user", "content": message.content})
    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config,
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)

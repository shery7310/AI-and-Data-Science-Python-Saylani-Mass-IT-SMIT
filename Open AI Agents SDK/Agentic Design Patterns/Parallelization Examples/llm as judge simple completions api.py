import os
from openai import OpenAI, AsyncOpenAI
from dotenv import load_dotenv
load_dotenv(override=True)
import time
import asyncio



async def create_question():

    huihui_judge = AsyncOpenAI(base_url=os.getenv("huihui_base_url"), api_key="not_needed")

    messages = [
        {
            "role": "user",
            "content": (
                "Create a difficult reasoning question to judge LLMs and their outputs, "
                "keep question short, only ask question don't provide reason why you asked a question, "
                "Now respond this way do not include markdown format"
                "Do not repeat Question"
            )
        }
    ]

    response = await huihui_judge.chat.completions.create(model= os.getenv("current_huihui_model"),
                                                messages= messages, stream= False)
    print("Created Question...")

    return f"""{response.choices[0].message.content}"""
    # return "For beginners is C better or Rust?" # Sample Question


question = asyncio.run(create_question())


async def answer_question():

    mistral = AsyncOpenAI(base_url= os.getenv("mistral_base_url"),
                         api_key= os.getenv("mistral"))

    huihui_llama_local = AsyncOpenAI(base_url=os.getenv("huihui_base_url"), api_key="not_needed")

    gemini = AsyncOpenAI(base_url=os.getenv("gemini_base_url"), api_key= os.getenv("gemini"))

    messages_huihui = [ # this is a local model and hallucinates a lot
                        # this is why i had to add specific instructions to it
        {
            "role": "user",
            "content": (f"""Answer this question to best of knowledge: {question},
                        Now respond this way do not include markdown format,
                        Do not keep repeating yourself in answer""")
        }
    ]

    messages = [
        {
            "role": "user",
            "content": f"Answer this question to best of knowledge: {question}"
        }
    ]
    
    mistral_model_name = os.getenv("mistral_model_name")
    huihui_model_name = os.getenv("current_huihui_model")
    gemini_model_name = os.getenv("gemini-2.5-flash")

    print("Answering Question Parallely...")

    mistral_response = await mistral.chat.completions.create(model= mistral_model_name,
                                                             messages=messages,
                                                             stream=False)

    huihui_response = await huihui_llama_local.chat.completions.create(model= huihui_model_name,
                                                             messages=messages_huihui,
                                                             stream=False)

    gemini_response = await gemini.chat.completions.create(model=gemini_model_name,
                                                             messages=messages,
                                                             stream=False)

    print("Local Models do take time though...")

    return {mistral_model_name: mistral_response.choices[0].message.content,
              huihui_model_name: huihui_response.choices[0].message.content,
              gemini_model_name: gemini_response.choices[0].message.content}

answer = asyncio.run(answer_question())

time.sleep(5) # added because of gemini, so we delay multiple requests to gemini

async def judge_question():
    gemini_judge = AsyncOpenAI(base_url=os.getenv("gemini_base_url"), api_key=os.getenv("gemini"))

    print(f"Models used: {answer.keys()}")

    messages = [
        {
            "role": "user",
            "content": ( f"""Judge which LLM answered this question: {question} best?
                        {answer}""")
        }
    ]

    print("Judging Question...")

    response = await gemini_judge.chat.completions.create(model=os.getenv("gemma-3n-e4b-it"),
                                                          messages=messages, stream=False)

    return f"""{response.choices[0].message.content}"""


print(asyncio.run(judge_question()))

"""
Sample Output:
Created Question...
Answering Question Parallely...
Local Models do take time though...
Models used: dict_keys(['ministral-8b-2410', 'huihuillama3.1-8k', 'gemini-2.5-flash'])
Judging Question...
The LLM that answered the question is **gemini-2.5-flash**.

Here's why:

* **Strong Emphasis on Rust for Beginners:** Gemini-2.5-flash clearly states that "For **most beginners**, Rust is a better choice than C..." and provides detailed reasons why, focusing on memory safety, tooling (Cargo), and error messages. This aligns with the current trend and the benefits Rust offers to newcomers.
* **Detailed Comparison:** The response provides a thorough and well-organized comparison of C and Rust, outlining pros and cons for beginners in a structured manner.
* **Addresses the "Best" Language:** Gemini-2.5-flash explicitly states Rust is better for most beginners and provides specific scenarios where C might be considered, effectively addressing the "best" aspect of the question.
* **Modern Language Focus:** The language used and the points made (like modern features in Rust) reflect a contemporary understanding of introductory programming education.
* **Structure and Formatting:** The use of headings, bullet points, and bold text makes the information easy to read and digest, a characteristic of Gemini's responses.

While the other LLM (`ministral-8b-2410`) provides a reasonable comparison, it leans more towards a more traditional view of starting with C for foundational knowledge. Gemini-2.5-flash's perspective is more aligned with the current recommendation for beginners in systems programming.
"""

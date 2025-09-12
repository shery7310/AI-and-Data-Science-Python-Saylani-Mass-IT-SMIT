import json

from agents import Agent,OpenAIChatCompletionsModel,Runner,function_tool, RunConfig
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_model = "gemini-2.5-flash"

gemini_api_key =os.getenv("gemini")
if not gemini_api_key:
    print("Properly add your api key")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(model= gemini_model, openai_client= external_client)

config = RunConfig(model = model, tracing_disabled = True, model_provider = external_client)

@function_tool()
def fetch_todos():
    """
    Retrieve and display the current list of to-do items.
    """
    try:
       print("fetching todos....")
       with open("todos.json","r") as file:
           data = json.load(file)
           return data
    except Exception as e:
        print(f"Error: {e}")
        raise FileNotFoundError("The file todos.json was not found.")

@function_tool()
def remove_todos(todo_id):
    """
            Removes todos based on todo_id, todo_id is the same as index number of the
            dictionaries in list of dictionaries

            Returns:
            json_data which holds the current dictionaries of todos in a form of a list
    """
    todo_id = int(todo_id)
    json_data = json.load(open('todos.json')) # This reads todos to json in same directory
    json_data.pop(todo_id)
    json.dump(json_data, open('todos.json', 'w'))
    json_data = json.load(open('todos.json'))
    return json_data

@function_tool()
def add_todos():
    print("Enter username and press enter:\n")
    username = input()
    print("Enter todo, keep it concise and press enter:\n")
    todo = input()
    try:
        if len(todo) > 60:
            print("Todo Too Long")
            print("Enter todo again\n")
            todo = input()
            if len(todo) < 10:
                print("Enter todo again length is less than 10 alphabets\n")
                todo = input()
                if len(todo) < 10 or len(todo) > 60:
                    raise "Todo is unacceptable"
    except Exception("Todo is unacceptable"):
        return False

    """
        Adds a new todo taking username and todo from user, as inputs
        Automatically assigns a new id and sets completed is false by default
        It should take two inputs from the user i.e. username: str and todo: str
        and then pass these two arguments to add_todos() function
        
        Notes:
        - If the function prints Todo Too Long, then it should should take input again
        - If while entering todo again length of todo is less than 10 user should be asked to enter todo again
        - If still he enter wrong the exception is raised
        
        Returns:
        True if the new todos is added
        False if the todos has not been added
    """
    json_data = json.load(open('todos.json'))
    last_elem = len(json_data)
    todo_id = last_elem + 1
    todo_id = str(todo_id)
    completed = str(False).lower()
    new_todo = {todo_id: {"username": username, "todo": todo, "completed": completed}}
    try:
        json_data.append(new_todo)
        json.dump(json_data, open('todos.json', 'w'))
        return True
    except Exception as e:
        return f"Error: {e}"

@function_tool()
def set_todo_as_complete():
    print("Remember to Enter Valid todo id")
    todo_id = int(input("Enter todo id:\n"))
    json_data = json.load(open('todos.json')) # returns a list of dictionaries
    todo_dict = json_data[todo_id]
    todo_id = str(todo_id)
    todo_dict[todo_id]['completed'] = "true"
    json_data.insert(int(todo_id), todo_dict)
    del json_data[int(todo_id) + 1]
    json.dump(json_data, open('todos.json', 'w'))
    json_data = json.load(open('todos.json'))


agent = Agent(name= "Todo Assistant",
              instructions="You are an expert of todos. You can add, list, and complete todos.",
              model = model, tools = [fetch_todos, remove_todos, add_todos, set_todo_as_complete])

# query = "Fetch me starting 5 todos"
query2 = 'Remove first todo with id "0" and show me the remaining todos'
query = input("Enter Query:\n")
result = Runner.run_sync(agent, [{"role": "user", "content": query}], run_config = config )

print(result.final_output)

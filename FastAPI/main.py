import os
import datetime
from logging import exception

from fastapi import FastAPI, HTTPException, Request
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from enum import Enum
from fastapi.responses import JSONResponse


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

load_dotenv()

db_url = os.getenv("db_url")

app = FastAPI()

# Mount html files
templates = Jinja2Templates(directory="templates")
# Mount static files (for CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db_client():
    try:
        client = MongoClient(db_url)
        print("Connected to MongoDB")
        return client
    except Exception as e:
        print("Error connecting to DB:", e)
    return None

db_client = get_db_client()

def get_collection():
    db = db_client.get_database("personal_assistant")
    collection = db.get_collection("todos")
    return collection

collection = get_collection()
estimated_documents = collection.estimated_document_count()

class Priority(str, Enum):
    LOW = "low"
    HIGH = "high"

class TodoItem(BaseModel):
    taskId: int = estimated_documents + 1
    userId: str
    title: str
    completed: bool
    priority: Priority
    category: str
    notes: Optional[str] = None

    class Config:
        extra = "forbid"

@app.get("/")
def read_root():
    return {"status": "Server is running"}

@app.get("/todos-by-user-id/{user_id}")
async def todos_by_userid(user_id: str):
    # sample id 68c86882e944b9144237b5eb
    # todos = collection.find_one({"_id": ObjectId("68c86cbdb5914b8219987317")})
    # user_id = todos["userId"]
    todos_by_user = collection.find({"userId": user_id})
    todos = []
    for todo in todos_by_user:
        todo["_id"] = str(todo["_id"])
        todos.append(todo)
    return todos

@app.post("/add_todo")
def add_todo(todo: TodoItem):

    try:
        collection.insert_one(dict(todo))
        return "Successfully Added"
    except exception as e:
        return {"error": str(e)}

@app.patch("/update_todo")
def change_todo_status(user_id):
    todos_by_user = collection.find({"userId": user_id})
    todos = []
    for todo in todos_by_user:
        todo["_id"] = str(todo["_id"])
        todos.append(todo)

@app.get("/all_todos")
def change_todo_status():
    all_todos= collection.find({}) # it expects a dictionary and
                                  # we aren't passing a specific one so it fetches all
    todos = []
    for todo in all_todos:
        todo["_id"] = str(todo["_id"])
        todos.append(todo)
    return todos

@app.get("/show_todos/{user_id}")
def show_todos(request: Request, user_id: str = None, task_id: int = None):
    todos_by_user = collection.find({"userId": user_id})  # this will fetch all the
    # todos by user_id
    print(todos_by_user)
    todos = []
    for todo in todos_by_user:
        todo["_id"] = str(todo["_id"])
        todos.append(todo)
        # Render HTML template with context
    return templates.TemplateResponse(
        "todos.html",
                {
                    "request": request,
                    "user_id": user_id,
                    "todos": todos
                }
            )

@app.delete("/remove_todo/{task_id}")
def remove_todo(task_id: int):
    query_filter = {"taskId": task_id}
    result = collection.delete_one(query_filter)
    if result.deleted_count == 1:
        return JSONResponse(
            content={"message": f"Task {task_id} deleted successfully"},
            status_code=200
        )
    else:
        return JSONResponse(
            content={"error": "Task not found or already deleted"},
            status_code=404
        )


@app.get("/login")
def login():
    pass

@app.get("/sign_up")
def sign_up():
    pass
# authentication logic
# AI agents Logic
# Stream Todos

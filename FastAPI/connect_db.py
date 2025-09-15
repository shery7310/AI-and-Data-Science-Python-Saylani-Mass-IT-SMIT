import os
import datetime
from logging import exception

from fastapi import FastAPI, HTTPException
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from enum import Enum


load_dotenv()

db_url = os.getenv("db_url")

app = FastAPI()

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

@app.get("/todos/{user_id}")
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

@app.patch("update_todo")
def change_todo_status(user_id):
    pass

@app.delete("/remove_todo")
def remove_todo(user_id: str, task_id: int):
    todos_by_user = collection.find({"userId": user_id})
    todos = []
    for todo in todos_by_user:
        todo["_id"] = str(todo["_id"])
        todos.append(todo)

@app.get("/login")
def login():
    pass

@app.get("/sign_up")
def sign_up():
    pass
# authentication logic
# AI agents Logic
# Stream Todos
from fastapi import FastAPI
from pydantic import BaseModel
from routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

# Run with: uvicorn app:app --reload


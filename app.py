"""
README

Run the app
    uvicorn app:app --reload

"""

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

# Initialize FastAPI app
app = FastAPI()

# MongoDB Configuration
MONGO_URI = "mongodb://root:123@localhost:27017/?retryWrites=true&w=majority"
DATABASE_NAME = "todo_db"
COLLECTION_NAME = "todo"

# Connect to MongoDB
client = MongoClient(MONGO_URI) #  noqa
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
    """
    Fetch a To-Do item from MongoDB based on its ID.

    :param todo_id: The MongoDB ObjectId of the To-Do item
    :return: The To-Do item if found, otherwise a 404 error
    """
    try:
        todo = collection.find_one({"_id": todo_id})
        if not todo:
            raise HTTPException(status_code=404, detail="To-Do not found")
        # todo["_id"] = str(todo["_id"])  # Convert ObjectId to string for JSON response
        return todo
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

# Run the app using: uvicorn app:app --reload

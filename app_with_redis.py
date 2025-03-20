from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
import redis
import json

# Initialize FastAPI app
app = FastAPI()

# MongoDB Configuration
MONGO_URI = "mongodb://root:123@localhost:27017/?retryWrites=true&w=majority"
DATABASE_NAME = "todo_db"
COLLECTION_NAME = "todo"

# Redis Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PREFIX = "todo:"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Connect to Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)


@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
    """
    Fetch a To-Do item from Redis cache first, if not found, then check MongoDB.

    - If found in Redis, return from Redis.
    - If found in MongoDB, store in Redis for future use.
    - If not found in MongoDB, return 404 Not Found.
    """
    try:
        # Check Redis first
        redis_key = f"{REDIS_PREFIX}{str(todo_id)}"
        cached_todo = redis_client.get(redis_key)
        if cached_todo:
            return json.loads(cached_todo)  # Return cached data

        # If not found in Redis, check MongoDB
        todo = collection.find_one({"_id": todo_id})
        if not todo:
            raise HTTPException(status_code=404, detail="To-Do not found")

        # Convert ObjectId to string
        # todo["_id"] = str(todo["_id"])

        # Store in Redis for future use (cache for 1 hour)
        redis_client.setex(redis_key, 3600, json.dumps(todo))

        return todo
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

# Run the app using: uvicorn app_with_redis:app --reload

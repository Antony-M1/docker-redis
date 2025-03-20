'''
This script connects to a running MongoDB instance, generates fake To-Do records using the Faker package,
and inserts them into a "todo" collection in the "todo_db" database.
'''

import random
from faker import Faker
from pymongo import MongoClient
from datetime import datetime

# Configuration Constants
MONGO_URI = "mongodb://root:123@localhost:27017/?retryWrites=true&w=majority"
DATABASE_NAME = "todo_db"  # Database name
COLLECTION_NAME = "todo"  # Collection name
DEFAULT_RECORDS = 1000  # Default number of records to insert

# Initialize Faker
fake = Faker()


# MongoDB Connection
def get_db_connection():
    """Establish a connection to MongoDB."""
    client = MongoClient(MONGO_URI)
    return client[DATABASE_NAME]


# Generate Fake To-Do Data
def generate_todo(index):
    """Generate a single fake To-Do item."""
    return {
        "_id": index,
        "title": fake.sentence(nb_words=6),  # Random task title
        "status": random.choice(["pending", "in-progress", "completed"]),  # Random status
        "created_at": datetime.utcnow().isoformat()  # Current timestamp in ISO format
    }


# Insert Data into MongoDB
def insert_todo_records(record_count=DEFAULT_RECORDS):
    """
    Inserts the given number of records into the MongoDB collection.

    :param record_count: Number of To-Do records to insert
    """
    db = get_db_connection()
    collection = db[COLLECTION_NAME]

    todos = [generate_todo(index) for index in range(1, record_count+1)]  # Create list of fake todos
    result = collection.insert_many(todos)  # Insert data

    print(f"✅ Successfully inserted {len(result.inserted_ids)} records into '{COLLECTION_NAME}' collection.")


if __name__ == "__main__":
    insert_todo_records()  # Run the script with the default record count

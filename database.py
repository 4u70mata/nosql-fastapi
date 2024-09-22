from motor.motor_asyncio import AsyncIOMotorClient
import os

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = AsyncIOMotorClient(mongo_uri)  # Explicit connection URL
database = client.mydatabase
user_collection = database["users"]

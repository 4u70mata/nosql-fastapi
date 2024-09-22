from bson import ObjectId
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field, conint
from typing import List, Optional
from database import user_collection
from pymongo.errors import PyMongoError

app = FastAPI()

# Models:
class Tweet(BaseModel):
    content: str
    hashtags: List[str]

class User(BaseModel):
    name: str
    email: EmailStr
    age: conint(ge=18, le=100)  # Constrained int (age must be between 18 and 100)
    tweets: Optional[List[Tweet]] = None

class UserResponse(User):
    id: str

# Routes
@app.get("/users", response_model=List[UserResponse])
async def read_users():
    users = []
    async for user in user_collection.find():  # async iterator for non-blocking I/O
        user["id"] = str(user["_id"])
        users.append(user)
    return users

@app.post("/users", response_model=UserResponse)
async def create_user(user: User):
    try:
        result = await user_collection.insert_one(user.model_dump(exclude_none=True))
        user_response = UserResponse(id=str(result.inserted_id), **user.model_dump()) 
        return user_response
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Database error")

@app.get("/user/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID format")
    
    try:
        db_user = await user_collection.find_one({"_id": ObjectId(user_id)})
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        db_user["id"] = str(db_user["_id"])
        return db_user
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


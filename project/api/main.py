from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from project.db import get_collection  # Импорт функции подключения к коллекции

app = FastAPI()

# Модель сообщения
class Message(BaseModel):
    username: str
    text: str

# Эндпоинт для получения всех сообщений
@app.get("/api/v1/messages/")
async def get_messages():
    collection = get_collection()
    messages = list(collection.find({}, {'_id': 0}))  # Не возвращаем поле _id
    return {"messages": messages}

# Эндпоинт для добавления сообщения
@app.post("/api/v1/message/")
async def create_message(message: Message):
    collection = get_collection()
    message_data = {
        "username": message.username,
        "text": message.text,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    collection.insert_one(message_data)
    return {"message": "Message added successfully"}

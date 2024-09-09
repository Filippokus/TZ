import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from fastapi import HTTPException

# Загружаем переменные окружения из файла .env
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")  # Задаем значение по умолчанию, если MONGO_PORT не указан

if not MONGO_URL or not MONGO_DB_NAME:
    raise HTTPException(status_code=500, detail="Проблема с переменными окружения для MongoDB")

# Формируем полный URL с указанием порта
mongo_connection_string = f"{MONGO_URL}:{MONGO_PORT}"

# Подключение к MongoDB
client = AsyncIOMotorClient(mongo_connection_string)
db = client[MONGO_DB_NAME]

async def get_collection():
    try:
        return db['messages']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при подключении к коллекции MongoDB: {str(e)}")

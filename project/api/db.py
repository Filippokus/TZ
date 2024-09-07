import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

client = MongoClient(MONGO_URL)
db = client[MONGO_DB_NAME]

def get_collection():
    return db['messages']

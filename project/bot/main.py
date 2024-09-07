import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers import start, message, buttons  # Импортируем обработчики

# Загружаем переменные окружения из файла .env
load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота, диспетчер и хранилище для FSM
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрируем обработчики
start.register_handlers(dp)
message.register_handlers(dp)
buttons.register_handlers(dp)

# Функция для запуска бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

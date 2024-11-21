import logging

from pyrogram import Client, filters
from .config import config

class ValentineBot:
    def __init__(self):
        self.client = Client(
            "valentine_session",
            api_id= config.API_ID,
            api_hash= config.API_HASH,
            phone_number= config.PHONE_NUMBER
        )

    async def connect(self):
        try:
            await self.client.start()
            return True
        except Exception as e:
            logging.error(f"Ошибка подключения: {e}")
            return False

    async def send_valentine(self, recipient, message):
        try:
            # Форматируем текст валентинки
            valentine_text = f"❤️ Вам Валентинка.\n\nСообщение: {message} \n\nСделать валентинку можно по ссылке: {config.URL_SITE}"
            
            # Асинхронная отправка сообщения
            await self.client.send_message(recipient, valentine_text)
            return True
        except Exception as e:
            logging.error(f"Ошибка отправки валентинки: {e}")
            return False

    async def disconnect(self):
        await self.client.stop()

valentine_bot = ValentineBot()

# Функция для инициализации бота при старте приложения
async def init_valentine_bot():
    if await valentine_bot.connect():
        print("User Bot успешно подключен!")
    else:
        print("Не удалось подключить User Bot")

# Функция для отправки валентинки
async def send_valentine(recipient, message):
    return await valentine_bot.send_valentine(recipient, message)
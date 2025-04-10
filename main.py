import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import html
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from App.handlers import commands, messages
from App.database.models import Async_Main
from dotenv import load_dotenv

load_dotenv()

def Get_Text(a):
    return html.bold(html.quote(a))
TOKEN = os.environ.get("TOKEN")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

async def main():
    await Async_Main()
    dp = Dispatcher()

    dp.include_routers(commands.router, messages.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

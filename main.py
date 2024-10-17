import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import html
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from handlers import commands, messages


bot = Bot(token="7386338867:AAFsLTq3_2SC9UejIN94I34Q47vfZjYXUSQ", default=DefaultBotProperties(parse_mode="HTML"))

def Get_Text(a):
    return html.bold(html.quote(a))

async def main():
    dp = Dispatcher()

    dp.include_routers(commands.router, messages.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

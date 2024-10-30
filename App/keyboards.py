from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def KeyboardBuilder(buttons:list):
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.add(types.KeyboardButton(text=button))
        print(button)
    builder.adjust(4)
    return builder


start_keyboard = [
    [types.KeyboardButton(text="Архив"),types.KeyboardButton(text="Поиск")],
    [types.KeyboardButton(text="/help")]
]
start_keyboard_markup = types.ReplyKeyboardMarkup(keyboard=start_keyboard,resize_keyboard=True)
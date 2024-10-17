from aiogram import types



start_keyboard = [
    [types.KeyboardButton(text="Архив"),types.KeyboardButton(text="Поиск")],
    [types.KeyboardButton(text="/help")]
]
start_keyboard_markup = types.ReplyKeyboardMarkup(keyboard=start_keyboard,resize_keyboard=True)
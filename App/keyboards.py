from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from App.database.requests import Get_Kids

async def Keyboard_Builder(buttons:list):
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.add(types.KeyboardButton(text=button))
        print(button)
    builder.adjust(3)
    return builder


async def Get_Kids_Keyboard(id_kid):

    kids = await Get_Kids(str(id_kid))
    kids_titles = []
    if kids:
        for kid in kids:
            kids_titles.append(kid.title)
    builder = ReplyKeyboardBuilder()
    if id_kid != 1:
        builder.row(types.KeyboardButton(text="Меню"))
    for button in kids_titles:
        builder.add(types.KeyboardButton(text=button))
        print(button)
    builder.adjust(3)
    builder.row(types.KeyboardButton(text="Назад"))
    return builder



start_keyboard = [
    [types.KeyboardButton(text="Обучение"),types.KeyboardButton(text="Поиск")],
    [types.KeyboardButton(text="/help")]
]

search_menu_keyboard = [
    [types.KeyboardButton(text="Управление своими командами"),types.KeyboardButton(text="Поиск команды")],
    [types.KeyboardButton(text="Назад")]
]

team_menu_keyboard = [
    [types.KeyboardButton(text="Создать команду"),types.KeyboardButton(text="Изменить команду")],
    [types.KeyboardButton(text="Назад")]
]

last_keyboard = [
    [types.KeyboardButton(text="Назад")]
]


start_keyboard_markup = types.ReplyKeyboardMarkup(keyboard=start_keyboard,resize_keyboard=True)
search_menu_markup = types.ReplyKeyboardMarkup(keyboard=search_menu_keyboard, resize_keyboard=True)
team_menu_markup = types.ReplyKeyboardMarkup(keyboard=team_menu_keyboard, resize_keyboard=True)
last_markup = types.ReplyKeyboardMarkup(keyboard=last_keyboard, resize_keyboard=True)

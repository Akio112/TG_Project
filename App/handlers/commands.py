from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from App.keyboards import start_keyboard_markup
from App.database.requests import Set_User, Add_Catalog, Get_Kids, Change_Archive_State, Add_Team

router = Router()


@router.message(Command("start"))
async def Start(message: types.Message):
    await Set_User(message.from_user.id, message.from_user.full_name)
    await Change_Archive_State(message.from_user.id, "-1")
    await message.answer(
        "Привет, новый пользователь!Я бот для обучения информационной безопасности и поиска тиммейтов для CTF",
        reply_markup=start_keyboard_markup)

@router.message(Command("test")) # just for us
async def Test(message : types.Message):
    await Add_Team("first_team", "we are the best", 1)
    await Add_Team("second", "we are not the best", 1)
    # await Add_Catalog("обучение", "описание", -1)
    # await Add_Catalog("название 2", "описание 2", 1)
    # await Add_Catalog("название 3", "описание 3", 1)
    # kids = await Get_Kids(1)
    # print(kids)
    # for user in kids:
    #     print(user.title)

@router.message(Command("help"))
async def Help(message: types.Message):
    await message.answer(
        "Это чат бот для помощи освоения в информационной безопасности для новичков, тут есть разные команды, которые тебе помогут\n"
        "<b>/tutorial</b> - переместит тебя в архив, также как альтернатива, из первого меню ты можешь просто нажать кнопочку '/archive'\n"
        "<b>/teams</b> - переместит тебя в меню поиска и создания команд, из первого меню ты также можешь туда перейти просто нажав кнопочку '/teams'",
        reply_markup=start_keyboard_markup)

#@router.message(Command("archive"))
#async def Archive(message: types.Message):
#    await message.answer("Извините, в данный момент функция не доступна")

@router.message(Command("teams"))
async def Teams(message: types.Message):
    await message.answer("Извините, в данный момент функция не доступна")
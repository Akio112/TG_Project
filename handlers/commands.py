from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from keyboards import start_keyboard_markup

router = Router()


@router.message(Command("start"))
async def Start(message: types.Message):
    await message.answer(
        "Привет, новый пользователь!Я бот для обучение информационной безопасности и поиска тиммейтов для CTF",
        reply_markup=start_keyboard_markup)


@router.message(Command("help"))
async def Help(message: types.Message):
    await message.answer(
        "Это чат бот для помощи освоения в информационной безопасности для новичков, тут есть разные команды, которые тебе помогут\n"
        "<b>/archive</b> - переместит тебя в архив, также как альтернатива, из первого меню ты можешь просто нажать кнопочку '/archive'\n"
        "<b>/teams</b> - переместит тебя в меню поиска и создания команд, из первого меню ты также можешь туда перейти просто нажав кнопочку '/teams'",
        reply_markup=start_keyboard_markup)
@router.message(Command("archive"))
async def Archive(message: types.Message):
    await message.answer("Извините, в данный момент функция не доступна")

@router.message(Command("teams"))
async def Teams(message: types.Message):
    await message.answer("Извините, в данный момент функция не доступна")
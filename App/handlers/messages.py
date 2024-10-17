from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from App.keyboards import start_keyboard_markup
from App.handlers.commands import Archive, Teams
router = Router()

@router.message(F.text.lower() == "архив")
async def Archive_button(message: types.Message):
    await Archive(message)


@router.message(F.text.lower() == "поиск")
async def Teams_button(message: types.Message):
    await Teams(message)

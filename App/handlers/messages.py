from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from App.keyboards import start_keyboard_markup, KeyboardBuilder
from App.handlers.commands import Archive, Teams
from App.database.requests import Get_Description, Get_Kids, Get_User
from App.filters import InArchiveFilter
router = Router()


#@router.message(F.text.lower() == "архив")
#async def Archive_button(message: types.Message):
#    await Archive(message)


@router.message(F.text.lower() == "поиск")
async def Teams_button(message: types.Message):
    await Teams(message)

@router.message(InArchiveFilter())
async def ArchiveNow(message: types.Message):
    user = await Get_User(message.from_user.id)
    kids = await Get_Kids(user.archive_id)
    id_kid = -1;
    for kid in kids:
        if (kid.title.lower() == message.text.lower()):
            id_kid = kid.id
    answer_text = await Get_Description(id_kid)
    print((str)(id_kid))
    kids = await Get_Kids((str)(id_kid))
    kids_titles = []
    if (kids):
        for kid in kids:
            kids_titles.append(kid.title)
    keyboard = await KeyboardBuilder(kids_titles)
    await message.answer(answer_text, reply_markup= keyboard.as_markup(resize_keyboard=True))

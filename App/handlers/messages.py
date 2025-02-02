from aiogram import Router, F
from aiogram import types
from App.keyboards import start_keyboard_markup, Get_Kids_Keyboard
#from App.handlers.commands import Teams
from App.database.requests import Get_Catalog, Get_Kids, Get_User,Change_Archive_State
from App.filters import InArchiveFilter, MenuFilter

router = Router()

#router.message(F.text.lower() == "поиск")
#async def Teams_Button(message: types.Message):
#    await Teams(message)

@router.message(MenuFilter())
async def Main_Menu(message: types.Message):
    await Change_Archive_State(message.from_user.id, "-1")
    await message.answer(
        "Добро пожаловать в главное меню! Выберите куда вы хотите перейти в поиск или изучение",
        reply_markup=start_keyboard_markup)


@router.message(InArchiveFilter())
async def Archive_Now(message: types.Message):
    user = await Get_User(message.from_user.id)
    if message.text.lower() == "назад":
        catalog_now = await Get_Catalog(int(user.archive_id))
        answer_text = (await Get_Catalog(int(catalog_now.parent))).description
        keyboard = await Get_Kids_Keyboard(int(catalog_now.parent))
        await Change_Archive_State(user.tg_id, catalog_now.parent)
        await message.answer(answer_text, reply_markup= keyboard.as_markup(resize_keyboard=True))
    else:
        kids = await Get_Kids(user.archive_id)
        id_kid = -1
        for kid in kids:
            if (kid.title.lower() == message.text.lower()):
                id_kid = kid.id
        if id_kid == -1:
            id_kid = 1
        answer_text = (await Get_Catalog(id_kid)).description
        keyboard = await Get_Kids_Keyboard(id_kid)
        await Change_Archive_State(user.tg_id, str(id_kid))
        await message.answer(answer_text, reply_markup= keyboard.as_markup(resize_keyboard=True))

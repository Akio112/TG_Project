from aiogram import types
from aiogram.filters import BaseFilter
from App.database.requests import Get_Kids, Get_User


class InArchiveFilter(BaseFilter):
    def __init__(self):
         pass

    async def __call__(self, message: types.Message) -> bool:
        user = await Get_User(message.from_user.id)
        now_kids = await Get_Kids(user.archive_id)
        now_kids_titles = []
        if now_kids:
            for kid in now_kids:
                now_kids_titles.append(kid.title.lower())
        return message.text.lower() in now_kids_titles or message.text.lower() == "/archive" or message.text.lower() == "назад"
class MenuFilter(BaseFilter):
    def __init__(self):
         pass

    async def __call__(self, message: types.Message) -> bool:
        user = await Get_User(message.from_user.id)
        return message.text.lower() == "меню" or (message.text.lower() == "назад" and user.archive_id == "1")
from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message
from App.database.requests import Get_Description, Get_Kids, Get_User


class InArchiveFilter(BaseFilter):
    def __init__(self):
         pass

    async def __call__(self, message:Message) -> bool:
        user = await Get_User(message.from_user.id)
        now_kids = await Get_Kids(user.archive_id)
        now_kids_titles = []
        if now_kids:
            for kid in now_kids:
                now_kids_titles.append(kid.title.lower())
        return message.text.lower() in now_kids_titles
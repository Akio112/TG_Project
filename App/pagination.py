from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton
from App.database.requests import Get_Team


class Pagination(CallbackData, prefix="pag"):
    page: int

async def get_paginated_kb(page: int = 0) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    start_offset = page * 5
    end_offset = start_offset + 5
    teams = []
    buttons_row = []
    for i in range(start_offset, end_offset):
        team = await Get_Team(i+1)
        if (team):
            buttons_row.append(types.InlineKeyboardButton(text = str(i+1),
                                             callback_data="team" + str(team.id)))
        else:
            end_offset = i
            break
    if page > 0:
        buttons_row.append(
            types.InlineKeyboardButton(
                text="⬅️",
                callback_data=str(page-1),
            )
        )
    if end_offset == start_offset + 5 and await Get_Team(end_offset):
        buttons_row.append(
            types.InlineKeyboardButton(
                text="➡️",
                callback_data=str(page + 1),
            )
        )
    builder.row(*buttons_row)
    builder.row(types.InlineKeyboardButton(text="Выход", callback_data="exit"))
    return builder.as_markup()
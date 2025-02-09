from aiogram import Router, F
from aiogram import types
from aiogram.filters import  StateFilter
from aiogram.fsm.state import StatesGroup, State

from App.keyboards import start_keyboard_markup, Get_Kids_Keyboard, search_menu_markup, team_menu_markup, last_markup
#from App.handlers.commands import Teams
from App.database.requests import Get_Catalog, Get_Kids, Get_User,Change_Archive_State, Change_Search_State, Add_Team, Delete_Team, Give_Teams_User
from App.filters import InArchiveFilter, MenuFilter, InSearchFilter, MakeTeamFilter
from aiogram.fsm.context import FSMContext

router = Router()

#router.message(F.text.lower() == "поиск")
#async def Teams_Button(message: types.Message):
#    await Teams(message)



class FormTeam(StatesGroup):
    choosing_team_name = State()
    choosing_team_description = State()

@router.message(MenuFilter())
async def Main_Menu(message: types.Message):
    await Change_Archive_State(message.from_user.id, "-1") # type: ignore
    await message.answer(
        "Добро пожаловать в главное меню! Выберите куда вы хотите перейти в поиск или изучение",
        reply_markup=start_keyboard_markup)


@router.message(InArchiveFilter())
async def Archive_Now(message: types.Message):
    user = await Get_User(message.from_user.id) # type: ignore
    if message.text.lower() == "назад": # type: ignore
        catalog_now = await Get_Catalog(int(user.archive_state)) # type: ignore
        answer_text = (await Get_Catalog(int(catalog_now.parent))).description # type: ignore
        keyboard = await Get_Kids_Keyboard(int(catalog_now.parent)) # type: ignore
        await Change_Archive_State(user.tg_id, catalog_now.parent) # type: ignore
        await message.answer(answer_text, reply_markup= keyboard.as_markup(resize_keyboard=True))
    else:
        kids = await Get_Kids(user.archive_state) # type: ignore
        id_kid = -1
        for kid in kids: # type: ignore
            if (kid.title.lower() == message.text.lower()): # type: ignore
                id_kid = kid.id
        if id_kid == -1:
            id_kid = 1
        answer_text = (await Get_Catalog(id_kid)).description # type: ignore
        keyboard = await Get_Kids_Keyboard(id_kid)
        await Change_Archive_State(user.tg_id, str(id_kid)) # type: ignore
        await message.answer(answer_text, reply_markup= keyboard.as_markup(resize_keyboard=True))
@router.message(InSearchFilter())
async def SearchMenu(message: types.Message):
    user = await Get_User(message.from_user.id) # type: ignore
    await message.answer("Добро пожаловать в меню поиска, здесь вы можете найти или создать свою команду",
                         reply_markup= search_menu_markup)
    await Change_Search_State(user.tg_id, "1") # type: ignore

@router.message(FormTeam.choosing_team_name)
async def NameChosen(message: types.Message, state:FSMContext):
    print(1)
    await state.update_data(new_name = message.text)
    await message.answer("Пожалуйста напишите немного о команде")
    await state.set_state(FormTeam.choosing_team_description)
@router.message(FormTeam.choosing_team_description)
async def DescriptionChosen(message: types.Message, state: FSMContext):
    name_team = await state.get_data()
    user = await Get_User(message.from_user.id) # type: ignore
    await message.answer("Команда создана!")
    await Add_Team(name_team['new_name'], message.text, user.id)
    await message.answer(
        "Выберите, хотите ли вы создать новую команду или изменить информацию о прошлой команде",
        reply_markup=team_menu_markup)
    await Change_Search_State(user.tg_id, "2")  # type: ignore
    await state.clear()
@router.message(MakeTeamFilter())
async def Make_Team(message: types.Message, state: FSMContext):
    user = await Get_User(message.from_user.id) # type: ignore
    if (user.search_state == "1" and message.text.lower() == "управление своими командами"): # type: ignore
        await message.answer("Выберите, хотите ли вы создать новую команду или изменить информацию о прошлой команде",
            reply_markup=team_menu_markup)
        await Change_Search_State(user.tg_id, "2") # type: ignore
    elif (user.search_state == "2" ):
        if (message.text.lower() == "создать команду"):
            await message.answer("Напишите название команды")
            await state.set_state(FormTeam.choosing_team_name)
        elif(message.text.lower() == "изменить команду"):
            teams = await Give_Teams_User(user.tg_id)
            count_teams = 1
            text_to_message = "Выберите номер команды из списка:"
            for el in teams:
                text_to_message += "\n"+((str)(count_teams) + " " + el.name)
                count_teams+=1
            await message.answer(text_to_message, reply_markup=last_markup)
            await Change_Search_State(user.tg_id, "4")
        elif (message.text.lower() == "назад"):
            await SearchMenu(message)
    elif (user.search_state =="4"):
        teams = await Give_Teams_User(user.tg_id)
        teams_list =[]
        for el in teams:
            teams_list.append(el)
        if (message.text.lower() == "назад"):
            await message.answer(
                "Выберите, хотите ли вы создать новую команду или изменить информацию о прошлой команде",
                reply_markup=team_menu_markup)
            await Change_Search_State(user.tg_id, "2")
        elif ((int)(message.text) <= len(teams_list)):
            await Delete_Team(teams_list[(int)(message.text) - 1].id)
            print((int)(message.text) - 1)
            print(teams_list[(int)(message.text) - 1].name)
            await message.answer("Напишите название команды")
            await state.set_state(FormTeam.choosing_team_name)

        else:
            await message.answer("Некорректный номер")

#@router.message()
#async def Menu(message: types.Message):
#    user = await Get_User(message.from_user.id)
#    await Change_Archive_State(user.tg_id, "1")


from ssl import SSL_ERROR_SSL
from App.database.models import async_session
from App.database.models import User, Archive, Team
from sqlalchemy import select

#создание нового юзера
async def Set_User(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id = tg_id, name = name, archive_state = "-1", search_state = "-1"))
            await session.commit()

#информация про юзера
async def Get_User(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            return user

#информация про тайтл
async def Get_Catalog(catalog_id):
    async with async_session() as session:
        catalog = await session.scalar(select(Archive).where(Archive.id == catalog_id))

        if catalog:
            return catalog

# информация про тайтл
async def Get_Kids(parent_id):
    async with async_session() as session:
        kids = await session.scalars(select(Archive).where(Archive.parent == parent_id))
        
        if kids:
            return kids

# добавить каталог или лист
async def Add_Catalog(title, description, parent_id):
    async with async_session() as session:
        session.add(Archive(title = title, description = description, parent = parent_id))
        await session.commit()

# поменять state в архиве
async def Change_Archive_State(tg_id, new_state):
    async with async_session() as session:
        state = await session.scalar(select(User).where(User.tg_id == tg_id))
        if state:
            state.archive_state = new_state
            await session.commit()
            
# поменять state в поиске
async def Change_Search_State(tg_id, new_state):
    async with async_session() as session:
        state = await session.scalar(select(User).where(User.tg_id == tg_id))
        if state:
            state.search_state = new_state
            await session.commit()     
            
# получить команду в бд
async def Get_Team(team_id):
    async with async_session() as session:
        team = await session.scalar(select(Team).where(Team.id == team_id))

        if team:
            return team
    
# добавить команду в бд    
async def Add_Team(name, description, author_id):
    async with async_session() as session:
        session.add(Team(name = name, description = description, author_id = author_id))
        await session.commit()
        
# удалить команду с бд
async def Delete_Team(id):
    async with async_session() as session:
        team = await session.scalar(select(Team).where(Team.id == id))
        if team:
            await session.delete(team)
            print("-маслина")
        await session.commit()
        
# выдать все команды владелец которых имеет tg_id
async def Give_Teams_User(tg_id):
    async with async_session() as session:
        user = await Get_User(tg_id)
        if user:
            teams = await session.scalars(select(Team).where(Team.author_id == user.id))
            return teams
        return None

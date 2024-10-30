from App.database.models import async_session
from App.database.models import User, Archive
from sqlalchemy import select

#создание нового юзера
async def Set_User(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id = tg_id, name = name, archive_id = "-1"))
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
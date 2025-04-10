import asyncio

from sqlalchemy import BigInteger, Column, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from sqlalchemy.sql import func

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger, unique=True)
    name: Mapped[str]
    archive_state: Mapped[str]
    search_state: Mapped[str]

class Archive(Base):
    __tablename__ = 'archive'

    id: Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str]
    description : Mapped[str]
    parent : Mapped[str | None]

class Team(Base):
    __tablename__ = 'team'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    author_id = Column(Integer, ForeignKey("users.id"))
    chat_id: Mapped[int]

async def Async_Main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all) # use to restart database(delete it)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(Async_Main())

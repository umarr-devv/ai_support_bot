from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.baked import Result

from src.models import User


async def create_user(sessions: async_sessionmaker, user_id: int) -> User:
    user = User(user_id=user_id)
    async with sessions() as session:
        session.add(user)
        await session.commit()
    return user


async def get_user_by_user_id(sessions: async_sessionmaker, user_id: int) -> User:
    sql = select(User).where(User.user_id == user_id).order_by(User.id)
    async with sessions() as session:
        result: Result = await session.execute(sql)
    return result.scalar()


async def get_user_by_id(sessions: async_sessionmaker, id: int) -> User:
    sql = select(User).where(User.id == id).order_by(User.id)
    async with sessions() as session:
        result: Result = await session.execute(sql)
    return result.scalar()


async def get_all_users(sessions: async_sessionmaker) -> list[User]:
    sql = select(User).order_by(User.id)
    async with sessions() as session:
        result: Result = await session.execute(sql)
    return result.scalars().all()

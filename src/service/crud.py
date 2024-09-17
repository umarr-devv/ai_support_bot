from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.baked import Result

from src.models import User, Prompt


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


async def create_promt(sessions: async_sessionmaker,
                       content: str,
                       prompt_id: int = 1) -> Prompt:
    prompt = Prompt(promt_id=1, content=content)
    async with sessions() as session:
        session.add(prompt)
        await session.commit()
    return prompt


async def update_prompt(sessions: async_sessionmaker,
                        content: str,
                        prompt_id: int = 1):
    sql = update(Prompt).where(Prompt.promt_id == prompt_id).values(content=content)
    async with sessions() as session:
        await session.execute(sql)
        await session.commit()


async def get_prompt(sessions: async_sessionmaker,
                     prompt_id: int = 1) -> Prompt:
    sql = select(Prompt).where(Prompt.promt_id == prompt_id)
    async with sessions() as session:
        result: Result = await session.execute(sql)
        await session.commit()
    return result.scalar()

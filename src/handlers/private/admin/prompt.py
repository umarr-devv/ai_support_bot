from aiogram import types, Router, Bot
from aiogram.filters.command import Command, CommandObject
from sqlalchemy.ext.asyncio import async_sessionmaker
from src.service.crud import create_promt, update_prompt, get_prompt
from src.service.crud import get_user_by_user_id

router = Router()


@router.message(Command(commands=['prompt']))
async def on_update_prompt(message: types.Message,
                           command: CommandObject,
                           sessions: async_sessionmaker):
    content = command.args
    if not content:
        text = '❌ Не был укзана промпт'
        await message.answer(text=text)
        return
    prompt = await get_prompt(sessions)

    if not prompt:
        await create_promt(sessions, content=content)
    else:
        await update_prompt(sessions, content=content)
    text = 'Успех'
    await message.answer(text)

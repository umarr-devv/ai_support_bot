from aiogram import types, Router, F
from aiogram.filters import CommandStart, CommandObject, Command

router = Router()


@router.message(Command(commands=['help']))
async def on_help(message: types.Message):
    text = 'Информация о компании'
    await message.answer(text=text)

from aiogram import types, Router, F
from aiogram.filters import CommandStart, CommandObject

router = Router()


@router.message(F.text == '📒 О компании')
async def on_about_company(message: types.Message):
    text = 'Информация о компании'
    await message.answer(text=text)


@router.message(F.text == '❕ О боте')
async def on_about_bot(message: types.Message):
    text = 'Информация о боте'
    await message.answer(text=text)

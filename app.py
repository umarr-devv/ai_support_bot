import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import Config
from src.handlers import router
from src.service.database import DataBase
from src.utils.logs import set_logging
from src.service.ai import AiApiClient
from src.models import Base

CONFIG_FILE = 'local-config.yml'

config = Config.create(config_file=CONFIG_FILE)
dp = Dispatcher(storage=MemoryStorage())
database = DataBase(config=config)
bot = Bot(token=config.bot.token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
ai_client = AiApiClient(config)


async def main():
    set_logging(config=config)

    dp.include_router(router)

    try:
        await dp.start_polling(bot, sessions=database.sessions,
                               config=config, ai_client=ai_client)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())

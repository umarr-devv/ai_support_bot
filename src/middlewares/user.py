from aiogram import types
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from src.service.crud import get_user_by_user_id, create_user


class UserMiddleware(BaseMiddleware):

    async def __call__(self,
                       handler,
                       event: types.Message | types.CallbackQuery,
                       data: dict) -> any:
        sessions = data.get('sessions')
        user_id = event.from_user.id

        user = await get_user_by_user_id(sessions, user_id)
        
        if not user:
            user = await create_user(sessions, user_id)

        data['user'] = user

        return await handler(event, data)

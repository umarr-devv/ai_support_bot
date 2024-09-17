from aiogram import Router

from src.filters.chat import AdminFilter
from src.handlers.private.admin.info import router as info_router

router = Router()

router.include_router(info_router)
router.message.filter(AdminFilter())
router.callback_query.filter(AdminFilter())

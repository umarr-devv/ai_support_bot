from aiogram import Router

from src.filters.chat import AdminFilter
from src.handlers.private.admin.info import router as info_router
from src.handlers.private.admin.prompt import router as prompt_router

router = Router()

router.include_router(info_router)
router.include_router(prompt_router)
router.message.filter(AdminFilter())
router.callback_query.filter(AdminFilter())

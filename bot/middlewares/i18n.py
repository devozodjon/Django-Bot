from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from bot.utils.db_commands.translation import get_user_language
from django.utils.translation import activate

class TranslationMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user_id = None

        if isinstance(event, Message) and event.from_user:
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery) and event.from_user:
            user_id = event.from_user.id

        if user_id:
            language = await get_user_language(user_id)
            activate(language)
            data['user_language'] = language
        else:
            activate('uz')
            data['user_language'] = 'uz'

        return await handler(event, data)

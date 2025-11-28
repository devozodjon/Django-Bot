import logging
from aiogram import Bot, Dispatcher
from django.apps import AppConfig
from core import config

logger = logging.getLogger(__name__)


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'

    bot: Bot = None
    dp: Dispatcher = None

    def ready(self):
        if BotConfig.bot is not None:
            return

        logger.info("Initializing bot...")

        BotConfig.bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
        BotConfig.dp = Dispatcher()

        # CORRECT middleware registration
        from bot.middlewares.i18n import TranslationMiddleware
        BotConfig.dp.update.middleware(TranslationMiddleware())

        # Register handlers
        from bot.handlers import start, menu, backs, ordering
        BotConfig.dp.include_router(start.router)
        BotConfig.dp.include_router(menu.router)
        BotConfig.dp.include_router(backs.router)
        BotConfig.dp.include_router(ordering.router)

        logger.info("Bot initialized successfully")

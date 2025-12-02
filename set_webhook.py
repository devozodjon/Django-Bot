import asyncio
from aiogram import Bot
from core import config

async def main():
    # Bot obyektini alohida yaratamiz
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)

    # Webhook URL o'rnatish
    await bot.set_webhook(
        url=f"{config.BASE_WEBHOOK_URL}{config.WEBHOOK_PATH}",
        drop_pending_updates=True
    )

    # Webhook info olish
    info = await bot.get_webhook_info()
    print("Webhook o'rnatildi:", info.url)
    print("Pending update count:", info.pending_update_count)

    await bot.session.close()  # Bot sessiyasini yopish

if __name__ == "__main__":
    asyncio.run(main())

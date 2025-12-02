import json
import logging
import asyncio
from aiogram.types import Update
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from bot.apps import BotConfig
from core import config

logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST
async def webhook(request):
    """
    Async webhook endpoint for receiving Telegram updates
    """
    try:
        update_data = json.loads(request.body.decode('utf-8'))
        update = Update(**update_data)

        # Process update with registered handlers
        await BotConfig.dp.feed_update(bot=BotConfig.bot, update=update)

        return JsonResponse({'status': 'ok'})

    except Exception as e:
        logger.error(f"Webhook error: {e}", exc_info=True)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def set_webhook_view(request):
    from asgiref.sync import async_to_sync

    try:
        url = f"{config.BASE_WEBHOOK_URL}{config.WEBHOOK_PATH}"
        async_to_sync(BotConfig.bot.set_webhook)(
            url=url,
            drop_pending_updates=True
        )
        info = async_to_sync(BotConfig.bot.get_webhook_info)()
        return JsonResponse({
            'status': 'success',
            'webhook_info': {
                'url': info.url,
                'pending_update_count': info.pending_update_count
            }
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


async def webhook_info_view(request):
    """Get webhook info"""
    try:
        webhook_info = await BotConfig.bot.get_webhook_info()

        return JsonResponse({
            'status': 'success',
            'webhook_info': {
                'url': webhook_info.url,
                'has_custom_certificate': webhook_info.has_custom_certificate,
                'pending_update_count': webhook_info.pending_update_count,
                'last_error_date': webhook_info.last_error_date,
                'last_error_message': webhook_info.last_error_message,
                'max_connections': webhook_info.max_connections,
            }
        })

    except Exception as e:
        logger.error(f"Webhook info error: {e}", exc_info=True)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def health_check(request):
    """Health check endpoint"""
    return JsonResponse({'status': 'ok'})


@csrf_exempt
def set_webhook_sync(request):
    async def set_webhook():
        url = f"{config.BASE_WEBHOOK_URL}{config.WEBHOOK_PATH}"
        await BotConfig.bot.set_webhook(url=url, drop_pending_updates=True)
        info = await BotConfig.bot.get_webhook_info()
        return {
            'url': info.url,
            'pending_update_count': info.pending_update_count
        }

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        info = loop.run_until_complete(set_webhook())
    finally:
        loop.close()

    return JsonResponse({'status': 'success', 'webhook_info': info})
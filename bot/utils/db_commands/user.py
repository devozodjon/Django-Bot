from asgiref.sync import sync_to_async
from bot.models import User

async def get_user(chat_id: int):
    return await sync_to_async(User.objects.filter(chat_id=chat_id).first)()

async def add_user(data: dict):
    return await sync_to_async(User.objects.create)(
        full_name=data.get("full_name"),
        phone_number=data.get("phone_number"),
        chat_id=data.get("chat_id"),
        location=data.get("location")
    )

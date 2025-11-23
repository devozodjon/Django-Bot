import logging

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from asgiref.sync import sync_to_async

# from bot.models import UserImage

logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "👋 Hello! Bot is working! 🎉\n\n"
        "📸 Send me an image and I'll save its file_id to the database.",
        parse_mode=None  # Override the default parse mode
    )
#
#
# @router.message(F.photo)
# async def handle_photo(message: Message):
#     """Handle incoming photos"""
#     try:
#         photo = message.photo[-1]
#
#         logger.info(f"Received photo from user {message.from_user.id}")
#
#         # Save to database
#         image = await sync_to_async(UserImage.objects.create)(
#             user_id=message.from_user.id,
#             username=message.from_user.username,
#             file_id=photo.file_id,
#             file_unique_id=photo.file_unique_id,
#             caption=message.caption
#         )
#
#         logger.info(f"Image saved with ID: {image.id}")
#
#         # Simple response without parse mode
#         await message.answer(
#             f"✅ Image saved!\n\n"
#             f"ID: {image.id}\n"
#             f"File ID: {photo.file_id}\n"
#             f"Size: {photo.width}x{photo.height}",
#             parse_mode=None
#         )
#
#         # Send the image back
#         await message.answer_photo(
#             photo=photo.file_id,
#             caption="Here's your image using the saved file_id!"
#         )
#
#     except Exception as e:
#         logger.error(f"Error: {e}", exc_info=True)
#         await message.answer("❌ Error saving image", parse_mode=None)
#
#
# @router.message(F.text)
# async def echo_handler(message: Message):
#     logger.info(f"Received: {message.text}")
#     # Escape markdown special characters
#     if message.text:
#         # Replace markdown special chars to avoid parsing errors
#         safe_text = message.text.replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace('`', '\\`')
#         await message.answer(f"Echo: {safe_text}")
#     else:
#         await message.answer("Echo: (empty)", parse_mode=None)
#
#
# @router.message()
# async def other_types_handler(message: Message):
#     await message.answer("Please send me a photo or text message", parse_mode=None)
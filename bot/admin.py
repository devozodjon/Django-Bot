import os
from asgiref.sync import async_to_sync
from aiogram.types import BufferedInputFile
from django.contrib import admin
from bot.apps import BotConfig
from bot.models.base import City
from bot.models.product import Product, Category
from core import config

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption_short', 'created_at']
    list_filter = ['created_at']
    search_fields = ['caption', 'file_id']
    readonly_fields = ['file_id', 'file_unique_id', 'created_at']

    def caption_short(self, obj):
        if obj.caption:
            return obj.caption[:50] + '...' if len(obj.caption) > 50 else obj.caption
        return '-'

    caption_short.short_description = "Caption"

    def save_model(self, request, obj, form, change):
        if obj.temp_file and not obj.file_id:
            try:
                obj.temp_file.seek(0)

                file_id, file_unique_id = async_to_sync(self._upload_to_telegram_async)(
                    obj.temp_file, obj.caption
                )

                existing = Product.objects.filter(file_unique_id=file_unique_id).first()
                if existing:
                    obj.temp_file.delete(save=False)
                    self.message_user(
                        request,
                        f"This image already exists in the database (ID: {existing.id}). Telegram file_unique_id: {file_unique_id}. You can reuse the existing file_id: {existing.file_id}",
                        level='WARNING'
                    )
                    return

                obj.file_id = file_id
                obj.file_unique_id = file_unique_id

                super().save_model(request, obj, form, change)

                if obj.temp_file:
                    obj.temp_file.delete(save=False)

                self.message_user(
                    request,
                    f"✅ Image uploaded to Telegram successfully! File ID: {file_id}",
                    level='SUCCESS'
                )

            except Exception as e:
                if obj.temp_file:
                    obj.temp_file.delete(save=False)

                self.message_user(
                    request,
                    f"❌ Error uploading to Telegram: {str(e)}",
                    level='ERROR'
                )
                raise
        else:
            super().save_model(request, obj, form, change)

    async def _upload_to_telegram_async(self, file_field, caption=None):
        storage_chat_id = getattr(config, 'TELEGRAM_STORAGE_CHAT_ID', None)

        if not storage_chat_id:
            raise ValueError(
                "TELEGRAM_STORAGE_CHAT_ID not set in settings. "
                "Please add your Telegram user ID or channel ID to settings.py"
            )

        file_content = file_field.read()
        file_name = os.path.basename(file_field.name)

        input_file = BufferedInputFile(
            file=file_content,
            filename=file_name
        )

        result = await self._send_to_telegram(
            BotConfig.bot,
            storage_chat_id,
            input_file,
            caption
        )

        return result['file_id'], result['file_unique_id']

    @staticmethod
    async def _send_to_telegram(bot, chat_id, input_file, caption):
        message = await bot.send_photo(
            chat_id=chat_id,
            photo=input_file,
            caption=caption
        )

        return {
            'file_id': message.photo[-1].file_id,
            'file_unique_id': message.photo[-1].file_unique_id
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
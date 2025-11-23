from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "chat_id", "location", "created_at", "updated_at")
    search_fields = ("full_name", "phone_number", "chat_id", "location")
    list_filter = ("created_at", "updated_at", "location")
    ordering = ("-created_at",)

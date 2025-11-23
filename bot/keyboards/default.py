from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇬🇧 English")
        ]
    ],
    resize_keyboard=True
)

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱Share phone number",request_contact=True)
        ]
    ],resize_keyboard=True
)
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

phone_number_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Telefon raqamni ulash", request_contact=True)
        ]
    ],
    resize_keyboard=True
)


languages_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇬🇧 English")
        ]
    ],
    resize_keyboard=True
)

phone_number_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Share phone number", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

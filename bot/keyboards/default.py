from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def phone_number_uz():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📱 Telefon raqamni ulash", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )


def phone_number_en():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📱 Share phone number", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )


def languages_en():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇺🇿 Uzbek"),
                KeyboardButton(text="🇬🇧 English")
            ]
        ],
        resize_keyboard=True
    )

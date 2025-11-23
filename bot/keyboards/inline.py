from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇬🇧 English")
        ],
    ],
    resize_keyboard=True
)

cities_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Farg'ona")
        ],
        [
            KeyboardButton(text="Samarqand"),
            KeyboardButton(text="Buxoro")
        ],
        [
            KeyboardButton(text="Andijon"),
            KeyboardButton(text="Namangan")
        ],
        [
            KeyboardButton(text="Nukus"),
            KeyboardButton(text="Qarshi")
        ],
        [
            KeyboardButton(text="Marg'ilon"),
            KeyboardButton(text="Qo'qon")
        ]
    ],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Buyurtma berish")
        ],
        [
            KeyboardButton(text="📖 Buyurtmalar tarixi")
        ],
        [
            KeyboardButton(text="⚙️ Sozlash"),
            KeyboardButton(text="🔥 Aksiya")
        ],
        [
            KeyboardButton(text="👨‍👩‍👧 Jamoamizga qo'shiling"),
            KeyboardButton(text="☎️ Les Ailes bilan aloqa")
        ]
    ],
    resize_keyboard=True
)

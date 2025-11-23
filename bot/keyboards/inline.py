from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

languages_uz = ReplyKeyboardMarkup(
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

main_menu_uz = ReplyKeyboardMarkup(
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


languages_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇬🇧 English")
        ],
    ],
    resize_keyboard=True
)

cities_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tashkent"),
            KeyboardButton(text="Fergana")
        ],
        [
            KeyboardButton(text="Samarkand"),
            KeyboardButton(text="Bukhara")
        ],
        [
            KeyboardButton(text="Andijan"),
            KeyboardButton(text="Namangan")
        ],
        [
            KeyboardButton(text="Nukus"),
            KeyboardButton(text="Karshi")
        ],
        [
            KeyboardButton(text="Margilan"),
            KeyboardButton(text="Kokand")
        ]
    ],
    resize_keyboard=True
)

main_menu_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Place Order")
        ],
        [
            KeyboardButton(text="📖 Order History")
        ],
        [
            KeyboardButton(text="⚙️ Settings"),
            KeyboardButton(text="🔥 Promotions")
        ],
        [
            KeyboardButton(text="👨‍👩‍👧 Join Our Team"),
            KeyboardButton(text="☎️ Contact Les Ailes")
        ]
    ],
    resize_keyboard=True
)

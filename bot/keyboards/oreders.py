from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

order_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏃 Olib ketish"),
            KeyboardButton(text="🚙 Yetkazib berish")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],resize_keyboard=True
)

take_away = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="📍 Eng yaqin filialni aniqlash")
        ],
        [
            KeyboardButton(text="🌐 Bu yerda buyurtma berish"),
            KeyboardButton(text="Filialni tanlang")
        ]
    ],resize_keyboard=True
)

delivery = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Eng yaqin filialni aniqlash"),
            KeyboardButton(text="🗺 Mening manzillarim")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],resize_keyboard=True
)
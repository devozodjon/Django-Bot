from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

order_list_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏃 Olib ketish"),
            KeyboardButton(text="🚙 Yetkazib berish")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],
    resize_keyboard=True
)

take_away_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="📍 Eng yaqin filialni aniqlash")
        ],
        [
            KeyboardButton(text="🌐 Bu yerda buyurtma berish"),
            KeyboardButton(text="Filialni tanlang")
        ]
    ],
    resize_keyboard=True
)

delivery_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Eng yaqin filialni aniqlash"),
            KeyboardButton(text="🗺 Mening manzillarim")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],
    resize_keyboard=True
)


order_list_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏃 Take Away"),
            KeyboardButton(text="🚙 Delivery")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ],
    resize_keyboard=True
)

take_away_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Back"),
            KeyboardButton(text="📍 Find Nearest Branch")
        ],
        [
            KeyboardButton(text="🌐 Order Here"),
            KeyboardButton(text="Select Branch")
        ]
    ],
    resize_keyboard=True
)

delivery_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Find Nearest Branch"),
            KeyboardButton(text="🗺 My Addresses")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ],
    resize_keyboard=True
)

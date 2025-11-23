from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

setting_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ismni o'zgartirish"),
            KeyboardButton(text="📱 Raqamni o'zgartirish")
        ],
        [
            KeyboardButton(text="🏙 Shaharni o'zgartirish"),
            KeyboardButton(text="🇺🇿 Tilni o'zgartirish")
        ],
        [
            KeyboardButton(text="ℹ️ Filallar haqida ma'lumotlar"),
            KeyboardButton(text="📄 Ommaviy taklif")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗣 Biz bilan aloqaga chiqing"),
            KeyboardButton(text="💬 Fikr bildirish")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],resize_keyboard=True
)
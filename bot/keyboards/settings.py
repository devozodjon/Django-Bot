from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

setting_menu_uz = ReplyKeyboardMarkup(
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

contact_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗣 Biz bilan aloqaga chiqing"),
            KeyboardButton(text="💬 Fikr bildirish")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],
    resize_keyboard=True
)

setting_menu_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Change Name"),
            KeyboardButton(text="📱 Change Phone")
        ],
        [
            KeyboardButton(text="🏙 Change City"),
            KeyboardButton(text="🇺🇿 Change Language")
        ],
        [
            KeyboardButton(text="ℹ️ Branch Info"),
            KeyboardButton(text="📄 Terms & Conditions")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ],
    resize_keyboard=True
)

contact_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗣 Contact Us"),
            KeyboardButton(text="💬 Feedback")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ],
    resize_keyboard=True
)

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards.default import languages_en, phone_number_uz, phone_number_en
from bot.keyboards.inline import main_menu_uz, main_menu_en, cities_uz, cities_en
from bot.state.register import UserState
from bot.utils.db_commands.user import get_user, add_user

router = Router()


@router.message(F.text == "/start")
async def start_handler(message: Message, state: FSMContext):
    user = await get_user(chat_id=message.chat.id)

    if user:
        lang = getattr(user, "language", "🇺🇿 Uzbek")
        if "🇬🇧 English" in lang:
            await message.answer("Welcome 😊", reply_markup=main_menu_en)
        else:
            await message.answer("Xush kelibsiz 😊", reply_markup=main_menu_uz)
    else:
        text = (
            "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n"
            "Tilni tanlang!\n\n"
            "Hello! Welcome to Les Ailes delivery service.\n"
            "Select language!"
        )
        await message.answer(text=text, reply_markup=languages_en)
        await state.set_state(UserState.language)


@router.message(UserState.language)
async def language_handler(message: Message, state: FSMContext):
    lang = message.text
    await state.update_data(language=lang)

    if "🇬🇧 English" in lang:
        await message.answer("Enter your full name:", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("To‘liq ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())

    await state.set_state(UserState.full_name)

@router.message(UserState.full_name)
async def full_name_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    await state.update_data(full_name=message.text)

    if "🇬🇧 English" in lang:
        await message.answer("📱 Send your phone number:", reply_markup=phone_number_en)
    else:
        await message.answer("📱 Telefon raqamingizni yuboring:", reply_markup=phone_number_uz)

    await state.set_state(UserState.phone_number)

@router.message(UserState.phone_number)
async def phone_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if message.contact:
        phone_number = message.contact.phone_number
    else:
        phone_number = message.text

    await state.update_data(phone_number=phone_number)

    if "🇬🇧 English" in lang:
        await message.answer("Select your city:", reply_markup=cities_en)
    else:
        await message.answer("Qaysi shaharda yashaysiz? Iltimos, shaharni tanlang:", reply_markup=cities_uz)

    await state.set_state(UserState.city)

@router.message(UserState.city)
async def city_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    await state.update_data(location=message.text)

    new_user = await add_user({
        "full_name": data.get("full_name"),
        "phone_number": data.get("phone_number"),
        "chat_id": message.chat.id,
        "location": data.get("location"),
    })

    if new_user:
        if "🇬🇧 English" in lang:
            text = (
                f"Registration successful ✅\n\n"
                f"Name: {data.get('full_name')}\n"
                f"Phone: {data.get('phone_number')}\n"
                f"City: {data.get('location')}\n"
            )
            menu_text = "Main menu"
            menu_kb = main_menu_en
        else:
            text = (
                f"Ro‘yxatdan muvaffaqiyatli o‘tildi ✅\n\n"
                f"Ism: {data.get('full_name')}\n"
                f"Telefon: {data.get('phone_number')}\n"
                f"Shahar: {data.get('location')}\n"
            )
            menu_text = "Bosh menyu"
            menu_kb = main_menu_uz
    else:
        if "🇬🇧 English" in lang:
            text = "Registration failed ❌"
            menu_text = "Main menu"
            menu_kb = main_menu_en
        else:
            text = "Ro‘yxatdan o‘tishda xatolik yuz berdi ❌"
            menu_text = "Bosh menyu"
            menu_kb = main_menu_uz

    await message.answer(text=text)
    await message.answer(text=menu_text, reply_markup=menu_kb)
    await state.clear()

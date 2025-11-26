from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.utils.db_commands.city import get_all_cities

from bot.keyboards.default import (
    languages_en,
    phone_number_uz,
    phone_number_en
)
from bot.keyboards.inline import (
    main_menu_uz,
    main_menu_en,
    build_cities_keyboard
)
from bot.state.register import UserState

from bot.utils.db_commands.translation import (
    get_user_language,
    set_user_language,
    get_or_create_user
)

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message, state: FSMContext):

    user, created = await get_or_create_user(
        user_id=message.chat.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

    if not created:
        lang = await get_user_language(message.chat.id)

        if lang == "en":
            await message.answer("Welcome 😊", reply_markup=main_menu_en())
        else:
            await message.answer("Xush kelibsiz 😊", reply_markup=main_menu_uz())
    else:
        text = (
            "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n"
            "Tilni tanlang!\n\n"
            "Hello! Welcome to Les Ailes delivery service.\n"
            "Select language!"
        )
        await message.answer(text=text, reply_markup=languages_en())
        await state.set_state(UserState.language)


@router.message(UserState.language)
async def language_handler(message: Message, state: FSMContext):

    lang_text = message.text

    if lang_text == "🇬🇧 English":
        await set_user_language(message.chat.id, "en")
        await message.answer("Enter your full name:", reply_markup=ReplyKeyboardRemove())
    elif lang_text == "🇺🇿 Uzbek":
        await set_user_language(message.chat.id, "uz")
        await message.answer("To‘liq ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Please select a language / Iltimos, tilni tanlang!", reply_markup=languages_en())
        return

    await state.update_data(language=lang_text)
    await state.set_state(UserState.full_name)



@router.message(UserState.full_name)
async def full_name_handler(message: Message, state: FSMContext):

    await state.update_data(full_name=message.text)

    lang_code = await get_user_language(message.chat.id)

    if lang_code == "en":
        await message.answer("📱 Send your phone number:", reply_markup=phone_number_en())
    else:
        await message.answer("📱 Telefon raqamingizni yuboring:", reply_markup=phone_number_uz())

    await state.set_state(UserState.phone_number)



@router.message(UserState.phone_number)
async def phone_handler(message: Message, state: FSMContext):

    if message.contact:
        phone_number = message.contact.phone_number
    else:
        phone_number = message.text

    await state.update_data(phone_number=phone_number)

    cities = await get_all_cities()
    city_names = [city.name for city in cities]

    lang_code = await get_user_language(message.chat.id)

    keyboard = build_cities_keyboard(city_names)

    if lang_code == "en":
        await message.answer("Select your city:", reply_markup=keyboard)
    else:
        await message.answer("Qaysi shaharda yashaysiz? Iltimos, tanlang:", reply_markup=keyboard)

    await state.set_state(UserState.city)



@router.message(UserState.city)
async def city_handler(message: Message, state: FSMContext):

    data = await state.get_data()
    lang_code = await get_user_language(message.chat.id)

    user, _ = await get_or_create_user(
        user_id=message.chat.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

    user.full_name = data["full_name"]
    user.phone_number = data["phone_number"]
    user.location = message.text
    await user.save()

    if lang_code == "en":
        text = (
            f"Registration successful ✅\n\n"
            f"Name: {data.get('full_name')}\n"
            f"Phone: {data.get('phone_number')}\n"
            f"City: {message.text}\n"
        )
        menu_text = "Main menu"
        menu_kb = main_menu_en()
    else:
        text = (
            f"Ro‘yxatdan muvaffaqiyatli o‘tildi ✅\n\n"
            f"Ism: {data.get('full_name')}\n"
            f"Telefon: {data.get('phone_number')}\n"
            f"Shahar: {message.text}\n"
        )
        menu_text = "Bosh menyu"
        menu_kb = main_menu_uz()

    await message.answer(text=text)
    await message.answer(menu_text, reply_markup=menu_kb)

    await state.clear()

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards.default import languages, phone_number
from bot.keyboards.inline import main_menu, cities_uz
from bot.state.register import UserState
from bot.utils.db_commands.user import get_user, add_user

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message, state: FSMContext):
    user = await get_user(chat_id=message.chat.id)
    if user:
        await message.answer("Welcome 😊", reply_markup=main_menu)
    else:
        text = (
            "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n"
            "Tilni tanlang!\n\n"
            "Hello! Welcome to Les Ailes delivery service.\n"
            "Select language!"
        )
        await message.answer(text=text, reply_markup=languages)
        await state.set_state(UserState.language)

@router.message(UserState.language)
async def language_handler(message: Message, state: FSMContext):
    await state.update_data(language=message.text)
    await message.answer("To‘liq ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserState.full_name)

@router.message(UserState.full_name)
async def full_name_handler(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("📱 Telefon raqamingizni yuboring:", reply_markup=phone_number)
    await state.set_state(UserState.phone_number)

@router.message(UserState.phone_number)
async def phone_handler(message: Message, state: FSMContext):
    # Contact orqali yuborsa yoki matn orqali yuborsa
    if message.contact:
        phone_number = message.contact.phone_number
    else:
        phone_number = message.text

    await state.update_data(phone_number=phone_number)
    await message.answer("Qaysi shaharda yashaysiz? Iltimos, shaharni tanlang:", reply_markup=cities_uz)
    await state.set_state(UserState.city)

@router.message(UserState.city)
async def city_handler(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    data = await state.get_data()

    new_user = await add_user({
        "full_name": data.get("full_name"),
        "phone_number": data.get("phone_number"),
        "chat_id": message.chat.id,
        "location": data.get("location"),
    })

    if new_user:
        text = (
            f"Ro‘yxatdan muvaffaqiyatli o‘tildi ✅\n\n"
            f"Ism: {data.get('full_name')}\n"
            f"Telefon: {data.get('phone_number')}\n"
            f"Shahar: {data.get('location')}\n"
        )
    else:
        text = "Ro‘yxatdan o‘tishda xatolik yuz berdi ❌"

    await message.answer(text=text)
    await message.answer(text="Bosh menyu", reply_markup=main_menu)
    await state.clear()

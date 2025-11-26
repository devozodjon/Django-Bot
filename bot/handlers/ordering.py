from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.inline import main_menu_uz, main_menu_en
from bot.keyboards.orders import (
    order_list_en, order_list_uz,
    take_away_en, take_away_uz,
    delivery_en, delivery_uz
)
from bot.keyboards.settings import setting_menu_uz, setting_menu_en, contact_uz, contact_en
from bot.state.register import UserState
from bot.utils.db_commands.translation import get_user_language

router = Router()

@router.message(F.text == "🛍 Buyurtma berish")
@router.message(F.text == "🛍 Place Order")
async def order_handler(message: Message, state: FSMContext):
    lang = await get_user_language(message.chat.id)
    await state.update_data(language=lang)

    if "🇬🇧 English" in lang:
        await message.answer("Select order type:", reply_markup=order_list_en())
    else:
        await message.answer("Buyurtma turini tanlang:", reply_markup=order_list_uz())

    await state.set_state(UserState.ordering)


@router.message(F.text == "🏃 Olib ketish")
@router.message(F.text == "🏃 Take Away")
async def take_away_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        await message.answer("Take away section:", reply_markup=take_away_en())
    else:
        await message.answer("Olib ketish bo‘limi:", reply_markup=take_away_uz())

    await state.set_state(UserState.take_away)


@router.message(F.text == "🚙 Yetkazib berish")
@router.message(F.text == "🚙 Delivery")
async def delivery_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        await message.answer("Delivery section:", reply_markup=delivery_en())
    else:
        await message.answer("Yetkazib berish bo‘limi:", reply_markup=delivery_uz())

    await state.set_state(UserState.delivery)


@router.message(F.text == "⚙️ Sozlash")
@router.message(F.text == "⚙️ Settings")
async def settings_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        await message.answer("You are in settings:", reply_markup=setting_menu_en())
    else:
        await message.answer("Sozlash bo‘limidasiz:", reply_markup=setting_menu_uz())

    await state.set_state(UserState.settings)


@router.message(F.text == "📖 Buyurtmalar tarixi")
@router.message(F.text == "📖 Order History")
async def history_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        await message.answer("🚫 You have no orders", reply_markup=main_menu_en())
    else:
        await message.answer("🚫 Sizda hech qanday buyurtma yo'q", reply_markup=main_menu_uz())


@router.message(F.text == "🔥 Aksiya")
@router.message(F.text == "🔥 Action")
async def action_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        await message.answer("🚫 No actions in your branch", reply_markup=main_menu_en())
    else:
        await message.answer("🚫 Sizning filialingizda hech qanday aksiya yo'q", reply_markup=main_menu_uz())


@router.message(F.text == "👨‍👩‍👧 Jamoamizga qo'shiling")
@router.message(F.text == "👨‍👩‍👧 Join our team")
async def group_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        await message.answer("You joined the team ✅", reply_markup=main_menu_en())
    else:
        await message.answer("Siz jamoga qo'shildingiz ✅", reply_markup=main_menu_uz())


@router.message(F.text == "☎️ Les Ailes bilan aloqa")
@router.message(F.text == "☎️ Contact Les Ailes")
async def contact_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        await message.answer("Contact us:", reply_markup=contact_en())
    else:
        await message.answer("Biz bilan aloqa:", reply_markup=contact_uz())

    await state.set_state(UserState.contact)


@router.message(F.text == "⬅️ Ortga")
@router.message(F.text == "⬅️ Back")
async def back_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    data = await state.get_data()
    lang = data.get("language")

    if "🇬🇧 English" in lang:
        menu_main = main_menu_en()
        text_main = "Main menu"
        text_order = "Select order type:"
        order_menu = order_list_en()
    else:
        menu_main = main_menu_uz()
        text_main = "Asosiy menyu"
        text_order = "Buyurtma turini tanlang:"
        order_menu = order_list_uz()

    if current_state in [str(UserState.take_away), str(UserState.delivery)]:
        await message.answer(text_order, reply_markup=order_menu)
        await state.set_state(UserState.ordering)
    else:
        await message.answer(text_main, reply_markup=menu_main)
        await state.clear()

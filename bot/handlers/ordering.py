from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.inline import main_menu
from bot.keyboards.oreders import order_list, take_away, delivery
from bot.keyboards.settings import setting_menu, contact
from bot.state.register import UserState

router = Router()


@router.message(F.text == "🛍 Buyurtma berish")
async def order_handler(message: Message, state: FSMContext):
    await message.answer("Buyurtma turini tanlang:", reply_markup=order_list)
    await state.set_state(UserState.ordering)


@router.message(F.text == "🏃 Olib ketish")
async def take_away_handler(message: Message, state: FSMContext):
    await message.answer("Olib ketish bo‘limi:", reply_markup=take_away)
    await state.set_state(UserState.take_away)


@router.message(F.text == "🚙 Yetkazib berish")
async def delivery_handler(message: Message, state: FSMContext):
    await message.answer("Yetkazib berish bo‘limi:", reply_markup=delivery)
    await state.set_state(UserState.delivery)



@router.message(F.text == "⚙️ Sozlash")
async def settings_handler(message: Message, state: FSMContext):
    await message.answer("Sozlash bo‘limidasiz:", reply_markup=setting_menu)
    await state.set_state(UserState.settings)



@router.message(F.text == "📖 Buyurtmalar tarixi")
async def history_handler(message: Message):
    await message.answer("🚫 Sizda hech qanday buyurtma yo'q", reply_markup=main_menu)



@router.message(F.text == "🔥 Aksiya")
async def action_handler(message: Message):
    await message.answer("🚫 Sizning filialingizda hech qanday aksiya yo'q", reply_markup=main_menu)



@router.message(F.text == "👨‍👩‍👧 Jamoamizga qo'shiling")
async def group_handler(message: Message):
    await message.answer("Siz jamoga qo'shildingiz ✅", reply_markup=main_menu)



@router.message(F.text == "☎️ Les Ailes bilan aloqa")
async def contact_handler(message: Message, state: FSMContext):
    await message.answer("Biz bilan aloqa:", reply_markup=contact)
    await state.set_state(UserState.contact)


@router.message(F.text == "⬅️ Ortga")
async def back_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state:
        if current_state in [
            str(UserState.take_away),
            str(UserState.delivery)
        ]:
            await message.answer("Buyurtma turini tanlang:", reply_markup=order_list)
            await state.set_state(UserState.ordering)

        elif current_state == str(UserState.ordering):
            await message.answer("Asosiy menyu:", reply_markup=main_menu)
            await state.clear()

        elif current_state == str(UserState.settings):
            await message.answer("Asosiy menyu:", reply_markup=main_menu)
            await state.clear()

        elif current_state == str(UserState.contact):
            await message.answer("Asosiy menyu:", reply_markup=main_menu)
            await state.clear()

        else:
            await message.answer("Asosiy menyu:", reply_markup=main_menu)
            await state.clear()
    else:
        await message.answer("Asosiy menyu:", reply_markup=main_menu)
        await state.clear()

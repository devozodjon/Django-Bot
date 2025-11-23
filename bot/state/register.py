from aiogram.fsm.state import State, StatesGroup

class UserState(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()
    city = State()
    ordering = State()
    take_away = State()
    delivery = State()
    settings = State()
    contact = State()

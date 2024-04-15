from aiogram.fsm.state import StatesGroup, State


class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_shift = State()
    fill_experience = State()
    fill_region = State()
    fill_additional_info = State()
    fill_consent = State()

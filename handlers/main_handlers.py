from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from keyboards.start import create_start_kb, create_conditions_kb
from FSMs.FSM import FSMFillForm


router = Router()


@router.message(
    Command(commands="start"),
    StateFilter(default_state),
)
async def process_start_command(
        message: Message,
        i18n: TranslatorRunner,
):
    await message.answer(
        text=i18n.command.start(),
        reply_markup=create_start_kb(i18n=i18n)
    )


@router.callback_query(
    F.data == "button-start",
    StateFilter(default_state)
)
async def process_press_start_button(
        callback: CallbackQuery,
        i18n: TranslatorRunner,
):
    await callback.message.answer(text=i18n.text.conditions())
    await callback.message.answer(
        text=i18n.text.conditions.list(),
        reply_markup=create_conditions_kb(i18n=i18n)
    )
    await callback.answer()


@ router.callback_query(F.data == "button-conditions-y")
async def process_press_start_button_1(
        callback: CallbackQuery,
        state: FSMContext,
        i18n: TranslatorRunner,
):
    await callback.message.answer(text=i18n.text.fill())
    await callback.message.answer(text=i18n.text.fill.name())
    await callback.answer()
    await state.set_state(FSMFillForm.fill_name)

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from keyboards.start import (
    create_start_kb,
    create_consent_kb,
    create_true_or_not_kb
)
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
    await callback.message.answer(text=i18n.text.consent())
    await callback.message.answer(
        text=i18n.text.consent.list(),
        reply_markup=create_consent_kb(i18n=i18n)
    )
    await callback.answer()


@router.callback_query(F.data == "button-consent-n")
async def process_press_consent_n(
        callback: CallbackQuery,
        i18n: TranslatorRunner,
):
    await callback.message.answer(text=i18n.text.consent.n())
    await callback.answer()


@router.callback_query(F.data == "button-consent-y")
async def process_press_consent_y(
        callback: CallbackQuery,
        state: FSMContext,
        i18n: TranslatorRunner,
):
    await callback.message.answer(text=i18n.text.fill())
    await callback.message.answer(text=i18n.text.fill.name())
    await callback.answer()
    await state.set_state(FSMFillForm.fill_name)


@router.message(
    StateFilter(FSMFillForm.fill_name),
    F.text.isalpha(),
)
async def process_name_sent(
        message: Message,
        state: FSMContext,
        i18n: TranslatorRunner,
):
    await state.update_data(fill_name=message.text)
    await message.answer(
        text=i18n.text.fill.name.is_true(name=message.text),
        reply_markup=create_true_or_not_kb(i18n=i18n, fill="name")
    )


@router.callback_query(F.data == "button-name-confirm-y")
async def process_press_name_confirm_y(
        callback: CallbackQuery,
        state: FSMContext,
        i18n: TranslatorRunner,
):
    await state.set_state(FSMFillForm.fill_age)
    await callback.message.answer(text=i18n.text.fill.age())
    await callback.answer()

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import default_state
from fluentogram import TranslatorRunner

from keyboards.start import create_start_kb


router = Router()


@router.message(Command(commands="start"), StateFilter(default_state))
async def process_start_command(message: Message, i18n: TranslatorRunner):
    await message.answer(
        text=i18n.command.start(),
        reply_markup=create_start_kb(i18n=i18n)
    )


@router.callback_query(F.data == "button-start")
async def process_press_start_button(callback: CallbackQuery):
    await callback.message.answer(text="11111")

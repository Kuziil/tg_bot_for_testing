from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from fluentogram import TranslatorRunner


router = Router()


@router.message(StateFilter(default_state))
async def send_echo(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.no.copy())

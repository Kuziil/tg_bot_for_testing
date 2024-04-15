from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import default_state
from fluentogram import TranslatorRunner


router = Router()


@router.message(Command(commands="start"), StateFilter(default_state))
async def process_start_command(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.command.start())

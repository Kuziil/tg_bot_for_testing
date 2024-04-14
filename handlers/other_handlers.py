from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state


other_handlers = Router()


@other_handlers.message(StateFilter(default_state))
async def send_echo(message: Message):
    await message.answer(text="1")

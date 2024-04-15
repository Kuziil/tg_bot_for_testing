from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluentogram import TranslatorRunner


def create_start_kb(
        i18n: TranslatorRunner
):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(
        text=i18n.button.start(),
        callback_data="button-start"
    ))
    return kb_builder.as_markup()

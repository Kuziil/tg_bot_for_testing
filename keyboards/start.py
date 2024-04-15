from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluentogram import TranslatorRunner


def create_start_kb(
        i18n: TranslatorRunner
):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=i18n.button.start(),
            callback_data="button-start"
        )
    )
    return kb_builder.as_markup()


def create_consent_kb(
        i18n: TranslatorRunner
):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=i18n.button.consent.y(),
            callback_data="button-consent-y"
        ),
        InlineKeyboardButton(
            text=i18n.button.consent.n(),
            callback_data="button-consent-n"
        ),
    )
    return kb_builder.as_markup()

def create_true_or_not_kb(
        i18n: TranslatorRunner,
        fill: str
):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=i18n.button.confirm.n(),
            callback_data=f"button-{fill}-confirm-n"
        ),
        InlineKeyboardButton(
            text=i18n.button.confirm.y(),
            callback_data=f"button-{fill}-confirm-y"
        ),
    )
    return kb_builder.as_markup()

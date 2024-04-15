import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from fluentogram import TranslatorHub

from config_data.config import Config, load_config
from handlers import other_handlers, main_handlers
from middlewares.i18n import TranslatorRunnerMiddleware
from utils.i18n import create_translator_hub

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    translator_hub: TranslatorHub = create_translator_hub()

    config: Config = load_config()

    dp.include_router(main_handlers.router)
    dp.include_router(other_handlers.router)

    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')

    dp.update.middleware(TranslatorRunnerMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub)

if __name__ == '__main__':
    asyncio.run(main())

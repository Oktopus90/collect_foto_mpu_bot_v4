import bot.handlers.start  # noqa
from bot.loader import bot_instance
from utils.logger import get_logger
import logging
import asyncio

log = get_logger(__name__)


async def run_bot() -> None:
    """Запуск оболочки бота."""
    log = get_logger(__name__)
    try:
        log.info('Bot started')
        await bot_instance.infinity_polling(
            skip_pending=True,
            logger_level=logging.INFO,
        )
        log.info('Bot stopped')
    except Exception as e:
        log.info(e)


async def main() -> None:
    """Запуск оболочки бота."""
    await asyncio.gather(
        run_bot(),
    )


if __name__ == '__main__':
    asyncio.run(
        main(),
    )

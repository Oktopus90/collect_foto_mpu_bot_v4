from bot.loader import bot_instance as bot
from telebot.types import Message
from utils.logger import get_logger

logger = get_logger(__name__)


@bot.message_handler(commands=['start'])
async def handle_start(message: Message) -> None:
    """Обработчик команды /start."""
    await bot.send_message(
        message.chat.id,
        f"Привет!!!!!!!{message.from_user.first_name}",
    )
    logger.info(f'{message.from_user.username} запустил бота')

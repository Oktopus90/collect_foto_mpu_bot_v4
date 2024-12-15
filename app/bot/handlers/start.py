from bot.crud.add_user import add_user
from bot.loader import bot_instance as bot
from telebot.types import Message
from utils.logger import get_logger

logger = get_logger(__name__)


@bot.message_handler(commands=['start'])
async def handle_start(message: Message) -> None:
    """Обработчик команды /start."""
    await bot.send_message(
        message.chat.id,
        f"Привет!! {message.from_user.first_name}",
    )
    data = {
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'telegram_id': message.from_user.id,
    }
    add_user(data)
    logger.info(f'{message.from_user.username} запустил бота')


@bot.message_handler(content_types=['text'])
async def echo_hand(message: Message) -> None:
    """Эхо чать."""
    await bot.send_message(
        message.chat.id,
        f"{message.from_user.first_name} написал: \n '{message.text}'",
    )

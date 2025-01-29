from bot import constants
from bot.loader import bot_instance as bot
from telebot.types import Message
from utils.logger import get_logger

logger = get_logger(__name__)
START_BUTTON_SEND_KP = constants.WELCOM_MENY[0]['Name']


@bot.message_handler(func=lambda message: message.text == START_BUTTON_SEND_KP)
async def start_send_kp(message: Message) -> None:
    """Начало сбора данных об КП."""
    await bot.send_message(
        message.chat.id,
        "Приступаем к сбору данных",
    )

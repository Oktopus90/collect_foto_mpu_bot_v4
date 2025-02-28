from bot import constants
from bot.loader import bot_instance as bot
from telebot.types import Message
from utils.logger import get_logger

logger = get_logger(__name__)
START_BUTTON_SEND_KP = constants.WELCOM_MENY[0]['Name']

user_state = {}
states = [
    'start',
    'adress',
    'coord',
    'age_category',
    'question',
    'discription',
    'comments',
    'photos',
]

def chek_state(message: Message, chek_state: str) -> bool:
    """Проверка сотсояния и id."""
    return user_state.get(message.chat.id, 0) == chek_state

    

@bot.message_handler(func=lambda message: message.text == START_BUTTON_SEND_KP)
async def start_send_kp(message: Message) -> None:
    """Начало сбора данных об КП."""
    await bot.send_message(
        message.chat.id,
        "Приступаем к сбору данных",
    )
    user_state[message.chat.id] = states[0]
    await bot.send_message(
        message.chat.id,
        f"Ваше состояние {user_state[message.chat.id]}",
    )
    user_state[message.chat.id] = states[1]

@bot.message_handler(func=lambda message: chek_state(message, 'adress'))
async def adress_send_kp(message: Message) -> None:
    """Начало сбора данных об КП."""
    user_state[message.chat.id] = states[0]
    await bot.send_message(
        message.chat.id,
        f"Ваше состояниеssds {user_state[message.chat.id]}",
    )

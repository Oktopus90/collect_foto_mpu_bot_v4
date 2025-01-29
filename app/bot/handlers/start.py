from bot import constants
from bot.crud.user import add_user, get_user_bd_from_tg_id
from bot.keyboards.generator import build_keyboard
from bot.loader import bot_instance as bot
from telebot.types import Message
from utils.logger import get_logger

logger = get_logger(__name__)


@bot.message_handler(commands=['start'])
async def handle_start(message: Message) -> None:
    """Обработчик команды /start."""
    user_bd = get_user_bd_from_tg_id(message.from_user.id)
    if user_bd:
        await bot.send_message(
            message.chat.id,
            f"С возвращением!! {user_bd.first_name}.\n"
            f"Вы впервые здесь были\n{user_bd.created_at}",
        )
    else:
        data = {
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'telegram_id': message.from_user.id,
        }
        add_user(data)
        await bot.send_message(
            message.chat.id,
            f"Приветствуем!! {message.from_user.first_name}.\n"
            f"Вы здесь впервые",
        )
    await bot.send_message(
        message.chat.id,
        "Ваши дальнейшие действия",
        reply_markup=await build_keyboard(
            menu_items=constants.WELCOM_MENY,
            is_inline=False,
        ),
    )
    logger.info(f'{message.from_user.username} запустил бота')


@bot.message_handler(content_types=['text'])
async def echo_hand(message: Message) -> None:
    """Эхо чать."""
    await bot.send_message(
        message.chat.id,
        f"{message.from_user.first_name} написал: \n '{message.text}'",
    )

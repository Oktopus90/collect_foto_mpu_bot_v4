from bot import constants
from bot.keyboards.generator import build_keyboard
from bot.keyboards.geopos import keyboard_geo
from bot.loader import bot_instance as bot
from telebot.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from utils.logger import get_logger


logger = get_logger(__name__)
START_BUTTON_SEND_KP = constants.WELCOM_MENY[0]['Name']

user_state = {}
states = [
    'start',
    'coord',
    'adress',
    'question',
    'comments',
    'photos',
    'final',
]
add_data = {
    'adres': '',
    'latitude': '',
    'longitude': '',
    'question': '',
    'comments': '',
    'photos': '',
 }


def chek_state(message: Message, chek_state: str) -> bool:
    """Проверка сотсояния и id."""
    print(">>>>>>>>>>", user_state.get(message.chat.id, 0))
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
        "Отправьте координаты",
        reply_markup=keyboard_geo,
    )
    user_state[message.chat.id] = states[1]


@bot.message_handler(content_types=["location"])
async def add_location(message: Message) -> None:
    """Запись координат."""
    if message.location is not None:
        add_data['latitude'] = message.location.latitude
        add_data['longitude'] = message.location.longitude
        await bot.send_message(
            message.chat.id,
            f"Ваши координаты: \n"
            f"latitude: {add_data['latitude']}\n"
            f"longitude: {add_data['longitude']}",
            reply_markup=ReplyKeyboardRemove(),
        )
        user_state[message.chat.id] = states[2]
        await bot.send_message(
            message.chat.id,
            "Введите адрес.",
        )


@bot.message_handler(func=lambda message: chek_state(message, 'coord'))
async def coord_send_kp(message: Message) -> None:
    """Получение координат."""
    if message.text == "Пропустить":
        user_state[message.chat.id] = states[2]
    else:
        await bot.send_message(
            message.chat.id,
            "Отправьте координаты",
            reply_markup=keyboard_geo,
        )


@bot.message_handler(func=lambda message: chek_state(message, 'adress'))
async def adress_send_kp(message: Message) -> None:
    """Получение адреса."""
    if message.text is not None:
        add_data['adres'] = message.text
        user_state[message.chat.id] = states[3]
        await bot.send_message(
            message.chat.id,
            "Напишите предварительный вопрос",
            reply_markup=ReplyKeyboardRemove(),
        )


@bot.message_handler(func=lambda message: chek_state(message, 'question'))
async def question_send_kp(message: Message) -> None:
    """Получение вопроса."""
    if message.text is not None:
        add_data['question'] = message.text
        user_state[message.chat.id] = states[4]
        await bot.send_message(
            message.chat.id,
            "Напишите комментарий.",
            reply_markup=ReplyKeyboardRemove(),
        )


@bot.message_handler(func=lambda message: chek_state(message, 'comments'))
async def comments_send_kp(message: Message) -> None:
    """Получение comments."""
    if message.text is not None:
        add_data['comments'] = message.text
        user_state[message.chat.id] = states[5]
        await bot.send_message(
            message.chat.id,
            "Пришлите фотографии",
            reply_markup=ReplyKeyboardRemove(),
        )

@bot.message_handler(content_types=['photo'])
async def send_photo(message: Message) -> None:
    print(message)
    file_info = await bot.get_file(message.photo[-1].file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    save_path = f'file{message.photo[-1].file_id}.jpg'  # сохраняем файл с его исходным именем
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    await bot.reply_to(message, 'Файл сохранен.')


@bot.message_handler(func=lambda message: chek_state(message, 'photos'))
async def photos_send_kp(message: Message) -> None:
    """Ожидание фотографий."""
    if message.text == "Пропустить":
        user_state[message.chat.id] = states[6]
    else:
        await bot.send_message(
            message.chat.id,
            "Отправьте фотографии",
        )
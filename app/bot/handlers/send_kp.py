import os

from bot import constants
from bot.keyboards.generator import build_keyboard
from bot.crud.kontrol_point import add_kontrol_point, get_next_number_kp
from bot.crud.user import get_user_bd_from_tg_id
from bot.keyboards.geopos import keyboard_geo
from bot.keyboards.utils import keyboard_next, keyboard_ok
from bot.loader import bot_instance as bot
from telebot.types import (
    Message,
    ReplyKeyboardRemove,
)
from utils.logger import get_logger
from utils.save_photo import save_photo

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
    'number': 0,
    'adres': '',
    'latitude': 0,
    'longitude': 0,
    'question': '',
    'comments': '',
    'photo': '',
    'discription': 'Здесь будет описание',
    'age_category': 'Здесь будет возрастная категория',
    'district': 'Здесь будет район',
 }


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
    add_data
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
    if chek_state(message, 'coord'):
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
    else:
        await bot.send_message(
            message.chat.id,
            "Что-то пошло не так. Перезапустите Бота\n Напишите /start",
            reply_markup=ReplyKeyboardRemove(),
        )


@bot.message_handler(func=lambda message: chek_state(message, 'coord'))
async def coord_send_kp(message: Message) -> None:
    """Получение координат."""
    if message.text.lower() == "пропустить":
        user_state[message.chat.id] = states[2]
        await bot.send_message(
            message.chat.id,
            "Введите адрес.",
        )
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
            reply_markup=keyboard_next,
        )


@bot.message_handler(content_types=['photo'])
async def send_photo(message: Message) -> None:
    """Сохранение фотографий."""
    if chek_state(message, 'photos'):
        file_info = await bot.get_file(message.photo[-1].file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        path_tmp_user = f"tmp/{message.chat.id}"
        if not os.path.isdir(path_tmp_user):
            os.mkdir(path_tmp_user)

        save_path = f'{path_tmp_user}/file_{message.photo[-1].file_id}.jpg'

        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        count_photo = len(os.listdir(path_tmp_user))
        await bot.send_message(
            message.chat.id,
            f'Было отправлено {count_photo}',
            reply_markup=keyboard_next,
        )
        add_data['photo'] = count_photo
    else:
        await bot.send_message(
            message.chat.id,
            "Что-то пошло не так. Перезапустите Бота\n Напишите /start",
            reply_markup=ReplyKeyboardRemove(),
        )


@bot.message_handler(func=lambda message: chek_state(message, 'photos'))
async def photos_send_kp(message: Message) -> None:
    """Ожидание фотографий."""
    if message.text == "Пропустить" or message.text == "Далее":
        user_state[message.chat.id] = states[6]
        await bot.send_message(
            message.chat.id,
            f"Отправка завершена. Всего было отправлено {add_data['photo']}",
            reply_markup=keyboard_next,
        )
    else:
        await bot.send_message(
            message.chat.id,
            "Отправьте фотографии",
        )


@bot.message_handler(func=lambda message: chek_state(message, 'final'))
async def final_send_kp(message: Message) -> None:
    """Завершение отправки КП."""
    if message.text == 'Далее':
        await bot.send_message(
            message.chat.id,
            "Теперь проверим отправленные данные.",
            reply_markup=ReplyKeyboardRemove(),
        )
        add_data['author'] = get_user_bd_from_tg_id(message.from_user.id)
        add_data['number'] = get_next_number_kp()
        s_msg = (f"Номер_кп: \t{add_data['number']}\n"
                 f"Автор: \t{add_data['author'].first_name}\n"
                 f"Адрес: \t{add_data['adres']}\n"
                 f"Вопрос: \t{add_data['question']}\n"
                 f"Коммент: \t{add_data['comments']}\n"
                 f"Щирота: \t{add_data['latitude']}\n"
                 f"Долгота: \t{add_data['longitude']}\n"
                 f"Кол-ов фото: \t{add_data['photo']}\n")
        await bot.send_message(
            message.chat.id,
            s_msg,
            reply_markup=keyboard_ok,
        )
    elif message.text == 'Ok':
        save_photo(message.chat.id, add_data['number'])
        add_kontrol_point(add_data)
        user_state[message.chat.id] = 'Нет'
        number = add_data['number']
        await bot.send_message(
            message.chat.id,
            f'Завершили отправку, добавлено КП №{number}',
            reply_markup=await build_keyboard(
                menu_items=constants.WELCOM_MENY,
                is_inline=False,
            ),
        )
    elif message.text == 'Не Ок':
        await bot.send_message(
            message.chat.id,
            "Еще раз отправьте данные по КП",
            reply_markup=await build_keyboard(
                menu_items=constants.WELCOM_MENY,
                is_inline=False,
            ),
        )
    else:
        await bot.send_message(
            message.chat.id,
            "Нажми на кнопку",
            reply_markup=keyboard_ok,
        )

from telebot.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


keyboard_geo = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_geo = KeyboardButton(
    text="Отправить геопозицию",
    request_location=True,
)

keyboard_geo.add(button_geo)
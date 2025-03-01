from telebot.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

keyboard_ok = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_ok = KeyboardButton(
    text="Ok",
)

keyboard_ok.add(button_ok)

keyboard_next = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_next = KeyboardButton(
    text="Завершить отправку",
)

keyboard_next.add(button_next)


from telebot.types import KeyboardButton, ReplyKeyboardMarkup

keyboard_ok = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_ok = KeyboardButton(
    text="Ok",
)
button_neok = KeyboardButton(
    text="Не Ок",
)

keyboard_ok.add(button_ok, button_neok)

keyboard_next = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_next = KeyboardButton(
    text="Далее",
)

keyboard_next.add(button_next)

from typing import List, TypedDict, Union

from bot import constants
from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


class MenuItem(TypedDict):
    """Определяет структуру данных для каждого элемента меню."""

    UniqueID: int
    Name: str


async def build_menu_buttons(
    menu_items: List[MenuItem],
    is_inline: bool = False,
) -> list:
    """Создаёт список кнопок меню."""
    accessible_items = menu_items
    if not accessible_items:
        if is_inline:
            return [
                [
                    InlineKeyboardButton(
                        constants.NO_ITEMS_TEXT,
                        callback_data=constants.NOOP,
                    ),
                ],
            ]
        return [[KeyboardButton(constants.NO_ITEMS_TEXT)]]

    def create_button(
        item: MenuItem,
    ) -> Union[InlineKeyboardButton, KeyboardButton]:
        if is_inline:
            callback_data = (
                f'{constants.SELECT_CALLBACK_PREFIX}'
                f'{item[constants.UNIQUE_ID_KEY]}'
            )
            return InlineKeyboardButton(
                text=item[constants.NAME_KEY],
                callback_data=callback_data,
            )
        return KeyboardButton(item[constants.NAME_KEY])

    buttons = [create_button(item) for item in accessible_items]
    return [
        buttons[i: i + constants.BUTTONS_PER_ROW]
        for i in range(0, len(buttons), constants.BUTTONS_PER_ROW)
    ]


async def build_keyboard(
    menu_items: List[MenuItem],
    is_inline: bool = False,
) -> Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]:
    """Создает клавиатуру (Reply или Inline)."""
    keyboard = await build_menu_buttons(
        menu_items,
        is_inline,
    )

    if is_inline:
        return InlineKeyboardMarkup(keyboard)
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for row in keyboard:
        reply_markup.row(*row)
    return reply_markup

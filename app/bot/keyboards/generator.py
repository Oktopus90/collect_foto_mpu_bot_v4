from math import ceil
from typing import List, Optional, Tuple, TypedDict, Union

from sqlalchemy.dialects.postgresql import UUID
from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from . import constants


NO_ITEMS_TEXT = 'Элементов нет'
NOOP = 'noop'
SELECT_CALLBACK_PREFIX ='select_'
UNIQUE_ID_KEY = 'UniqueID'
NAME_KEY = 'Name'
BUTTONS_PER_ROW = 1


class MenuItem(TypedDict):
    """Определяет структуру данных для каждого элемента меню."""

    UniqueID: int
    Name: str


async def build_menu_buttons(
    menu_items: List[MenuItem],
    is_inline: bool = False,
) -> list:
    """Создаёт список кнопок меню с учётом пагинации и доступности элементов."""
    accessible_items = menu_items
    if not accessible_items:
        if is_inline:
            return [
                [
                    InlineKeyboardButton(
                        NO_ITEMS_TEXT,
                        callback_data=NOOP,
                    ),
                ],
            ]
        return [[KeyboardButton(NO_ITEMS_TEXT)]]

    def create_button(
        item: MenuItem,
    ) -> Union[InlineKeyboardButton, KeyboardButton]:
        if is_inline:
            callback_data = (
                f'{SELECT_CALLBACK_PREFIX}'
                f'{item[UNIQUE_ID_KEY]}'
            )
            return InlineKeyboardButton(
                text=item[NAME_KEY],
                callback_data=callback_data,
            )
        return KeyboardButton(item[NAME_KEY])

    buttons = [create_button(item) for item in accessible_items]
    return [
        buttons[i: i + BUTTONS_PER_ROW]
        for i in range(0, len(buttons), BUTTONS_PER_ROW)
    ]


async def build_keyboard(
    menu_items: List[MenuItem],
    is_inline: bool = False,
) -> Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]:
    """Создает клавиатуру (Reply или Inline) с поддержкой иерархии и пагинации."""
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

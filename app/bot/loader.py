import os
from typing import Optional

from dotenv import load_dotenv
import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.states.asyncio.middleware import StateMiddleware

load_dotenv()
BOT_TOKEN: Optional[str] = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError('BOT_TOKEN is not set')
bot_instance = AsyncTeleBot(BOT_TOKEN)

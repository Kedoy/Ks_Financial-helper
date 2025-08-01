import asyncio
import logging
import os
from bot.settings import *
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from datetime import time, datetime
from aiogram.types import FSInputFile
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

bot = Bot(
    token=TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
        )
    )

dp = Dispatcher()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

from bot.handlers.start import *
from bot.handlers.expenses import *

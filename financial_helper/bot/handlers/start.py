from aiogram import types
from bot.dispatcher import dp
from aiogram.filters import Command

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Привет! Я финансовый помощник.")
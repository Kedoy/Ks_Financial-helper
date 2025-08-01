from django.core.management.base import BaseCommand
from ...settings import *
from bot.dispatcher import dp, bot
import os
import django
import asyncio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

class Command(BaseCommand):
    help = 'Запускает Telegram-бота'

    def handle(self, *args, **options):
        self.stdout.write("Бот запущен...")
        
        # await bot.send_message(
            #     chat_id=TELEGRAM_ADMIN_ID,
            #     text="Бот запущен!"
            #     )
            # await dp.start_polling(bot)

        async def start_polling():
            await dp.start_polling(bot)
        
        asyncio.run(start_polling())
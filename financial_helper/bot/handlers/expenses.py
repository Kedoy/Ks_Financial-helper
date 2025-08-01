from aiogram import types, F
from aiogram.filters import Command
from core.models import Expense
from asgiref.sync import sync_to_async
from bot.dispatcher import dp

@dp.message(Command('expenses'))
async def show_expenses(message: types.Message):
    expenses = await sync_to_async(list)(Expense.objects.select_related('category').all()[:10])
    
    if not expenses:
        await message.answer("Нет данных о расходах.")
        return

    response = "Последние расходы:\n"
    for expense in expenses:
        response += f"• {expense.amount} ₽ — {expense.category}\n"
    
    await message.answer(response)
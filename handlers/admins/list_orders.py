from aiogram import types

from data.config import ADMINS
from database.shop_data import get_all_orders, get_book
from loader import dp


@dp.message_handler(text='📃 Zakazlar ro\'yhati', user_id=ADMINS)
async def list_orders(message: types.Message):
    orders = get_all_orders()
    if not orders:
        await message.answer("Hali zakazlar yo'q")
    else:
        all_orders = '📃 Zakazlar ro\'yxati:\n\n'
        for order in orders:
            user_id, book_id = order[1], order[2]
            user_details = await dp.bot.get_chat(user_id)
            book_details = f"{get_book(book_id)[1]} kitobi - {get_book(book_id)[2]} so'm"
            all_orders += f"📘 {order[0]}-zakaz) {user_details.full_name} | {book_details}\n\n"
        await message.answer(all_orders)

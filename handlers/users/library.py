from aiogram import types

from database.shop_data import get_orders, get_book
from loader import dp


@dp.message_handler(text='🔖 Mening kutubxonam')
async def my_library(message: types.Message):
    orders = get_orders(message.from_user.id)
    books = '📗 Mening kitoblarim:\n\n'
    if not orders:
        await message.answer("Sizda hali kitob yo'q")
    else:
        for order in orders:
            book_id = order[2]
            books += f"{get_book(book_id)[1]} kitobi - {get_book(book_id)[2]} so'm\n"
        await message.answer(books)

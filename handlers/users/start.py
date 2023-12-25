from aiogram import types

from database.shop_data import check_user, add_user, create_users_table
from keyboards.default.books_kb import book_categories
from keyboards.default.start_kb import start_keyboards
from loader import dp


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    create_users_table()
    if check_user(message.from_user.id):
        await message.answer(f"Xush kelibsiz, {message.from_user.full_name}!", reply_markup=start_keyboards)
    else:
        add_user(message.from_user.id, message.from_user.full_name)
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=start_keyboards)


@dp.message_handler(text='📚 Kitoblarimiz')
async def bot_books(message: types.Message):
    await message.answer(f"Kitoblar kategoriyasini tanlang:", reply_markup=book_categories)

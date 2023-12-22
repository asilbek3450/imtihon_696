from aiogram import types

from keyboards.default.books_kb import book_categories
from keyboards.default.start_kb import start_keyboards
from loader import dp


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=start_keyboards)


@dp.message_handler(text='📚 Kitoblarimiz')
async def bot_books(message: types.Message):
    await message.answer(f"Kitoblar kategoriyasini tanlang:", reply_markup=book_categories)


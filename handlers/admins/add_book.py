from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import ADMINS
from database.shop_data import create_books_table, add_book
from keyboards.default.books_kb import book_categories
from keyboards.default.start_kb import start_admin_keyboards
from loader import dp


class AddBook(StatesGroup):
    name = State()
    price = State()
    photo = State()
    author = State()
    category_id = State()
    confirm = State()


@dp.message_handler(text='📖 Kitob qo\'shish', chat_id=ADMINS)
async def book(message: types.Message):
    create_books_table()
    await message.answer("Kitob nomini kiriting:", reply_markup=types.ReplyKeyboardMarkup(
        resize_keyboard=True, keyboard=[
            [types.KeyboardButton(text="⬅️ Orqaga")]
        ]
    ))
    await AddBook.name.set()


@dp.message_handler(state=AddBook.name)
async def add_book_name(message: types.Message, state: FSMContext):
    if message.text == "⬅️ Orqaga":
        await message.answer("Bosh sahifaga qaytdik", reply_markup=start_admin_keyboards)
        await state.finish()
    else:
        await state.update_data(name=message.text)
        await message.answer("Kitob narxini kiriting:", reply_markup=types.ReplyKeyboardRemove())
        await AddBook.price.set()


@dp.message_handler(state=AddBook.price)
async def add_book_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Kitob rasmini yuboring:")
    await AddBook.photo.set()


@dp.message_handler(state=AddBook.photo, content_types=[types.ContentType.PHOTO, types.ContentType.DOCUMENT])
async def add_book_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Kitob muallifini kiriting:")
    await AddBook.author.set()


@dp.message_handler(state=AddBook.author)
async def add_book_author(message: types.Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer("Kitob kategoriyasini tanlang:", reply_markup=book_categories)
    await AddBook.category_id.set()


@dp.message_handler(state=AddBook.category_id)
async def add_book_category_id(message: types.Message, state: FSMContext):
    await state.update_data(category_id=message.text.split(' ')[1])
    data = await state.get_data()
    await message.answer(f"Kitobni tasdiqlaysizmi?\n"
                         f"Kitob nomi: {data['name']}\n"
                         f"Kitob narxi: {data['price']}\n"
                         f"Kitob muallifi: {data['author']}\n"
                         f"Kitob kategoriyasi: {data['category_id']}",
                         reply_markup=types.ReplyKeyboardMarkup(
                             resize_keyboard=True, keyboard=[
                                 [types.KeyboardButton(text="✅ Ha"), types.KeyboardButton(text="❌ Yo'q")]
                             ]
                         ))
    await AddBook.confirm.set()


@dp.message_handler(state=AddBook.confirm)
async def add_book_confirm(message: types.Message, state: FSMContext):
    if message.text == "✅ Ha":
        data = await state.get_data()
        add_book(data['name'], data['price'], data['photo'], data['author'], data['category_id'])
        await message.answer("Kitob qo'shildi!", reply_markup=start_admin_keyboards)
        await state.finish()
    else:
        await message.answer("Kitob qo'shilmadi!", reply_markup=start_admin_keyboards)
        await state.finish()

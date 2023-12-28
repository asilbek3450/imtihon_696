from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import ADMINS
from database.shop_data import create_category_table, add_category
from keyboards.default.books_kb import book_categories
from keyboards.default.start_kb import start_admin_keyboards
from loader import dp


class AddCategory(StatesGroup):
    name = State()
    confirm = State()


@dp.message_handler(text='📈 Kategoriya qo\'shish', user_id=ADMINS)  # filterlari
async def category(message: types.Message):
    create_category_table()
    await message.answer("Kategoriya nomini kiriting:", reply_markup=types.ReplyKeyboardMarkup(
        resize_keyboard=True, keyboard=[
            [types.KeyboardButton(text="⬅️ Orqaga")]
        ]
    ))
    await AddCategory.name.set()


@dp.message_handler(state=AddCategory.name)
async def add_category_name(message: types.Message, state: FSMContext):
    if message.text == "⬅️ Orqaga":
        await message.answer("Bosh sahifaga qaytdik", reply_markup=start_admin_keyboards)
        await state.finish()
    else:
        await state.update_data(name=message.text)
        data = await state.get_data()
        await message.answer(f"Kategoriya nomini tasdiqlaysizmi? {data['name']}", reply_markup=types.ReplyKeyboardMarkup(
            resize_keyboard=True, keyboard=[
                [types.KeyboardButton(text="✅ Ha"), types.KeyboardButton(text="❌ Yo'q")]
            ]
        ))
        await AddCategory.confirm.set()


@dp.message_handler(state=AddCategory.confirm)
async def add_category_confirm(message: types.Message, state: FSMContext):
    if message.text == "✅ Ha":
        data = await state.get_data()
        add_category(data['name'])
        await message.answer("Kategoriya qo'shildi!", reply_markup=start_admin_keyboards)
        await state.finish()
    else:
        await message.answer("Kategoriya qo'shilmadi!", reply_markup=start_admin_keyboards)
        await state.finish()

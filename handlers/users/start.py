from aiogram import types

from database.shop_data import check_user, add_user, create_users_table
from keyboards.default.start_kb import start_keyboards, start_admin_keyboards
from loader import dp


@dp.message_handler(commands=['start'])  # admin bo'lmagan foydalanuvchi uchun start bosganida ishlaydi
async def bot_start(message: types.Message):
    create_users_table()
    if check_user(message.from_user.id):  # agar botda foydalanuvchi oldin /start ni bosgan bo'lsa
        await message.answer(f"Xush kelibsiz, {message.from_user.full_name}!", reply_markup=start_keyboards)
    else:  # aks holda, ya'ni botda yangi bo'lsa
        add_user(message.from_user.id, message.from_user.full_name)  # foydalanuvchini bazaga qo'shamiz
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=start_keyboards)

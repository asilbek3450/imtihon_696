from aiogram import types

from data.config import ADMINS
from database.shop_data import get_users
from loader import dp


@dp.message_handler(text='👥 Foydalanuvchilar ro\'yhati', user_id=ADMINS)
async def list_users(message: types.Message):
    users = get_users()
    if not users:
        await message.answer("Hali birorta foydalanuvchi yo'q")
    else:
        all_users = '<b>👥 Foydalanuvchilar ro\'yxati:</b>\n\n'
        for user in users:
            all_users += f"👤 {user[0]}-foydalanuvchi) {user[2]}\nTelegram id: {user[1]}\n\n"
        await message.answer(all_users)

from aiogram import types

from data.config import ADMINS
from keyboards.default.start_kb import start_admin_keyboards
from loader import dp


@dp.message_handler(commands=['start'], user_id=ADMINS)  # admin uchun start bosganida ishlaydi
async def admin_start(message: types.Message):
    await message.answer(f"👑 Xush kelibsiz admin aka, {message.from_user.full_name}!", reply_markup=start_admin_keyboards)


from aiogram import types

from data.config import ADMINS
from keyboards.default.location_kb import manzil
from keyboards.default.start_kb import start_keyboards, start_admin_keyboards
from loader import dp
from utils.get_location import choose_nearest_location


@dp.message_handler(text='📌 Manzillarimiz')
async def manzil_keyboard(message: types.Message):
    await message.reply("Joylashgan manzilingizni jo'nating", reply_markup=manzil)


@dp.message_handler(text='⬅️ Orqaga', chat_id=ADMINS)
async def orqaga_keyboard(message: types.Message):
    await message.reply("Bosh sahifaga qaytdik", reply_markup=start_admin_keyboards)


@dp.message_handler(text='⬅️ Orqaga')
async def orqaga_keyboard(message: types.Message):
    await message.reply("Bosh sahifaga qaytdik", reply_markup=start_keyboards)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    location = message.location
    latitude = message.location.latitude
    longitude = message.location.longitude

    # await message.answer_location(latitude=latitude, longitude=longitude)  # foydalanuvchi yuborgan manzilni qaytarish
    await message.answer(await choose_nearest_location(location), disable_web_page_preview=True)
    # disable_web_page_preview=True - bot xabar jo'natganda google maps linki pasida rasm chiqmasligi uchun


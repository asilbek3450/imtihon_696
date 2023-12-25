from aiogram import types

from keyboards.default.admin_kb import contact
from keyboards.default.start_kb import start_keyboards
from loader import dp


@dp.message_handler(text='✍️ Admin')
async def admin_handler(message: types.Message):
    await message.answer("Admin bilan bog'lanish uchun telefon raqamingizni qoldiring", reply_markup=contact)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact_handler(message: types.Message):
    phone_number = message.contact.phone_number
    text = f"📞 Telefon raqam: {phone_number} qabul qilindi!, siz bilan adminlarimiz bog'lanadi."
    await message.answer(text=text, reply_markup=start_keyboards)

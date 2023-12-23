from aiogram import types

from data.book_data import book_details
from data.config import ADMINS
from keyboards.default.books_kb import book_categories
from keyboards.default.start_kb import start_keyboards
from keyboards.inline.book_inlines import ertaklar, darsliklar, it_kitoblar, buyurtma
from loader import dp, bot


@dp.message_handler(text='📚 Ertaklar')
async def ertak_books(message: types.Message):
    await message.answer(f"{message.text} kategoriyasidagi kitoblardan birini tanlang:", reply_markup=ertaklar)


@dp.message_handler(text='📚 Darsliklar')
async def darslik_books(message: types.Message):
    await message.answer(f"{message.text} kategoriyasidagi kitoblardan birini tanlang:", reply_markup=darsliklar)


@dp.message_handler(text='📚 IT ga oid kitoblar')
async def it_books(message: types.Message):
    await message.answer(f"{message.text} kategoriyasidagi kitoblardan birini tanlang:", reply_markup=it_kitoblar)


@dp.callback_query_handler()
async def books_callback(call: types.CallbackQuery):
    call_data = call.data
    book_info = book_details.get(call_data)

    if book_info is not None:
        photo = book_info.get('photo')
        caption = book_info.get('caption')
        await call.message.answer_photo(photo=photo, caption=caption, reply_markup=buyurtma)
        await call.message.delete()

    elif call_data == 'buyurtma_berish':
        product_name = call.message.caption.split('\n')[0]
        product_price_without_currency = call.message.caption.split('\n')[1].split(' ')[0]
        for admin in ADMINS:
            await bot.send_message(chat_id=admin,
                                   text=f"Foydalanuvchi {call.from_user.full_name} - {call.from_user.id}\n"
                                        f"{product_name} kitob uchun buyurtma qoldirdi!")
        await call.message.answer(
            f"{product_name} kitob uchun buyurtma qabul qilindi! Tez orada siz bilan bog'lanamiz!\n"
            f"Kitob narxi: {product_price_without_currency} so'm\n",
            reply_markup=start_keyboards)

        await call.message.delete()

    elif call_data == 'back_to_categories':
        await call.message.edit_text('Kategoriyalardan birini tanlang:', reply_markup=book_categories)

    elif call_data == 'back_to_books':
        await call.message.answer_photo(photo=photo, caption=caption, reply_markup=buyurtma)

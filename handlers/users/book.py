from aiogram import types

from keyboards.inline.book_inlines import ertaklar, darsliklar, it_kitoblar, buyurtma
from loader import dp


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
    if call_data == 'garri_potter':
        photo = 'https://assets.asaxiy.uz/product/items/desktop/586f9b4035e5997f77635b13cc04984c2022050413390782248fkpwdXX3zG.jpg.webp'
        await call.message.answer_photo(photo=photo, caption='📚 Joanna Ketlin Rouling: Garri Potter va afsonaviy tosh', reply_markup=buyurtma)
    elif call_data == 'shum_bola':
        photo = 'https://assets.asaxiy.uz/product/items/desktop/6d6968d87c240c699190e2d8c029fa9d2022050917350580492gYLnCWqRTG.jpg.webp'
        await call.message.answer_photo(photo=photo, caption='📚 G\'afur G\'ulom: Shum bola', reply_markup=buyurtma)
    elif call_data == 'sariq_devni_minib':
        photo = 'https://assets.asaxiy.uz/product/items/desktop/5e15bf0c4d167.jpg.webp'
        await call.message.answer_photo(photo=photo, caption='📚 Xudoyberdi To‘xtaboyev: Sariq devni minib', reply_markup=buyurtma)

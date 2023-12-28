from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from database.shop_data import get_book, add_order, create_orders_table
from keyboards.default.books_kb import book_categories
from keyboards.inline.book_inlines import get_books_keyboards, buyurtma
from loader import dp, bot

category_id = None


@dp.message_handler(text='📚 Kitoblarimiz')
async def all_books(message: types.Message):
    await message.answer('Kategoriyalardan birini tanlang:', reply_markup=book_categories)


@dp.message_handler(text_startswith='📚')
async def books(message: types.Message):
    global category_id
    category_id = int(message.text.split('.')[0].split(' ')[1])
    await message.answer(f'{message.text} kategoriyasidagi kitoblar:', reply_markup=get_books_keyboards(category_id))


@dp.callback_query_handler()
async def books_callback(call: types.CallbackQuery):
    call_data = call.data

    if call_data.startswith('book_'):
        book_id = int(call_data.split('_')[-1])
        book = get_book(book_id)
        await call.message.answer_photo(photo=book[3], caption=f"<b>{book[0]} {book[1]}</b>\n\n"
                                                               f"Narxi: {book[2]} so'm\n\n"
                                                               f"Muallif: {book[4]}", reply_markup=buyurtma)

    elif call_data == 'buyurtma_berish':
        create_orders_table()

        book_id = int(call.message.caption.split(' ')[0])
        book = get_book(book_id)

        user_id = call.message.chat.id

        await call.message.answer(f"Siz {book[1]} kitobini buyurtma berdingiz!, \nNarxi {book[2]} so\'m."
                                  f"\nAdminlarimiz siz bilan bog\'lanishadi, xaridingiz uchun rahmat!"
                                  f"\n\nBosh sahifaga qaytish uchun /start ni bosing", reply_markup=ReplyKeyboardRemove())
        await bot.send_message(chat_id=ADMINS[0], text=f"🛒 Yangi buyurtma:\n"
                                                       f"Kitob nomi: {book[1]}\n"
                                                       f"Kitob narxi: {book[2]}\n"
                                                       f"Kitob muallifi: {book[4]}\n"
                                                       f"Buyurtmachi: {call.message.chat.full_name}\n"
                                                       f"Buyurtmachi id: {call.message.chat.id}")
        add_order(user_id, book_id)

    elif call_data == 'back_to_categories' or call_data == 'back_to_books':
        await call.message.delete()
        await call.message.answer('Kategoriyalardan birini tanlang:', reply_markup=book_categories)

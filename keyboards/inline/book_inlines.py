from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.shop_data import get_books

back_to_categories = InlineKeyboardButton('⬅️ Kategoriyalarga qaytish', callback_data='back_to_categories')


def get_books_keyboards(category_id):
    books = get_books(category_id)
    books_kb = InlineKeyboardMarkup(row_width=2)
    for book in books:
        books_kb.insert(
            InlineKeyboardButton(text=f"📚 {book[0]}. {book[1]}", callback_data=f"book_{book[0]}"))
    books_kb.add(back_to_categories)
    return books_kb


buyurtma = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('✅ Buyurtma berish', callback_data='buyurtma_berish')],
    [InlineKeyboardButton('⬅️ Orqaga', callback_data='back_to_books')],
])

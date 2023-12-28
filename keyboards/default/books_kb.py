from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from database.shop_data import get_categories

book_categories = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
for category in get_categories():
    book_categories.insert(KeyboardButton(text=f"📚 {category[0]}. {category[1]}"))

book_categories.add(KeyboardButton(text="⬅️ Orqaga"))

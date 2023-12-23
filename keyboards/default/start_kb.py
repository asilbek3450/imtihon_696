from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📚 Kitoblarimiz')],
    [KeyboardButton('🔖 Mening kutubxonam')],
    [KeyboardButton('📌 Manzillarimiz')],
    [KeyboardButton('✍️ Admin'), KeyboardButton('⚙️ Sozlamalar')]
])



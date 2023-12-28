from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📚 Kitoblarimiz')],
    [KeyboardButton('🔖 Mening kutubxonam')],
    [KeyboardButton('📌 Manzillarimiz')],
    [KeyboardButton('✍️ Admin'), KeyboardButton('⚙️ Sozlamalar')]
])

start_admin_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📚 Kitoblarimiz')],
    [KeyboardButton('🔖 Mening kutubxonam'), KeyboardButton('📌 Manzillarimiz')],
    [KeyboardButton('📈 Kategoriya qo\'shish'), KeyboardButton('📖 Kitob qo\'shish')],
    [KeyboardButton('👥 Foydalanuvchilar ro\'yhati')],
    [KeyboardButton('📃 Zakazlar ro\'yhati')],
    [KeyboardButton('✍️ Admin'), KeyboardButton('⚙️ Sozlamalar')]
])


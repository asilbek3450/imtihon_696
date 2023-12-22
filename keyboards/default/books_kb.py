from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

book_categories = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📚 Ertaklar'), KeyboardButton('📚 Darsliklar')],
    [KeyboardButton('📚 IT ga oid kitoblar'), KeyboardButton('📚 Ilmiy kitoblar')],
    [KeyboardButton('📚 Maqolalar'), KeyboardButton('📚 Romanlar')],
    [KeyboardButton('📚 Sherlar'), KeyboardButton('📚 Boshqa')],
    [KeyboardButton('⬅️ Bosh menyu')]
])

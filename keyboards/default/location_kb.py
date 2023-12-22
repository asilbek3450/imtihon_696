from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

manzil = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📌 Manzil jo\'natish', request_location=True)],
    [KeyboardButton('⬅️ Orqaga')]
])

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_to_categories = InlineKeyboardButton('⬅️ Kategoriyalarga qaytish', callback_data='back_to_categories')

ertaklar = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('📚 Joanna Ketlin Rouling: Garri Potter va afsonaviy tosh', callback_data='garri_potter')],
    [InlineKeyboardButton('📚 G\'afur G\'ulom: Shum bola', callback_data='shum_bola')],
    [InlineKeyboardButton('📚 Xudoyberdi To‘xtaboyev: Sariq devni minib', callback_data='sariq_devni_minib')],
])
ertaklar.add(back_to_categories)

darsliklar = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('📚 O\'zbekiston tarixi', callback_data='tarix')],
    [InlineKeyboardButton('📚 Matematika', callback_data='matematika')],
    [InlineKeyboardButton('📚 Ona tili', callback_data='ona_tili')],
    [InlineKeyboardButton('📚 Ingliz tili', callback_data='ingliz_tili')],
    [InlineKeyboardButton('📚 Fizika', callback_data='fizika')],
    [InlineKeyboardButton('📚 Kimyo', callback_data='kimyo')],
    [InlineKeyboardButton('📚 Biologiya', callback_data='biologiya')],
])
darsliklar.add(back_to_categories)

it_kitoblar = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('📚 Anvar Narzullayev: "Python"da dasturlash asoslari', callback_data='python')],
    [InlineKeyboardButton('📚 Jeymi Chan: Python 0 dan 100 gacha', callback_data='python_0dan100')],
])
it_kitoblar.add(back_to_categories)

buyurtma = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('✅ Buyurtma berish', callback_data='buyurtma_berish')],
    [InlineKeyboardButton('⬅️ Orqaga', callback_data='back_to_books')],
])

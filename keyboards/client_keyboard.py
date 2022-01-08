from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Ish tartibi ⏰')
b2 = KeyboardButton('Manzil 🗺')
b3 = KeyboardButton('/Menyu')
b4 = KeyboardButton("Telefon raqamingizni yuboring", request_contact=True)
b5 = KeyboardButton("Joylashgan joyingiz", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b3).add(b1).insert(b2).row(b4, b5)

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_load = KeyboardButton('/Yuklash')
button_delete = KeyboardButton('/O\'chirish')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)

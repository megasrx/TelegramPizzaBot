from aiogram import types, Dispatcher
from config import telegram_bot_username
from create_bot import dp, bot
from keyboards import kb_client
from data_base.sqlite_db import sql_read_command


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Salom! Yoqimli ishataha", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(
            f"Bot bilan chatda suhbatlashish uchun unga start buyrug'ini bering. {telegram_bot_username}")


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Har kuni, 24 soat")


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Toshkent shahri")


async def pizza_menu_command(message: types.Message):
    await sql_read_command(message)


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start', 'help'])
    dispatcher.register_message_handler(pizza_open_command, lambda message: 'Ish tartibi' in message.text)
    dispatcher.register_message_handler(pizza_place_command, lambda message: 'Manzil' in message.text)
    dispatcher.register_message_handler(pizza_menu_command, lambda message: 'Menyu' in message.text)

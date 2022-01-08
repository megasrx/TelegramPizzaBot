from aiogram import types, Dispatcher
from config import telegram_bot_username
from create_bot import dp, bot


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Salom! Yoqimli ishataha")
        await message.delete()
    except:
        await message.reply(
            f"Bot bilan chatda suhbatlashish uchun unga start buyrug'ini bering. {telegram_bot_username}")


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Har kuni, 24 soat")


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Toshkent shahri")


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start', 'help'])
    dispatcher.register_message_handler(pizza_open_command, commands=['Ish_tartibi'])
    dispatcher.register_message_handler(pizza_place_command, commands=['Manzil'])

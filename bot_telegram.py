from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import telegram_bot_token, telegram_bot_username


bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Bot online rejimda ishlamoqda.")


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Salom! Yoqimli ishataha")
        await message.delete()
    except:
        await message.reply(f"Bot bilan chatda suhbatlashish uchun unga start buyrug'ini bering. {telegram_bot_username}")


@dp.message_handler(commands=['Ish_tartibi'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Har kuni, 24 soat")


@dp.message_handler(commands=['Manzil'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Toshkent shahri")


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

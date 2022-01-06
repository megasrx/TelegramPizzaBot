from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import telegram_bot_token


bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)



executor.start_polling(dp, skip_updates=True)

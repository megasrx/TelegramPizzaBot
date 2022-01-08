from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print("Bot online rejimda ishlamoqda.")

from handlers import client
from handlers import admin
from handlers import others

client.register_handlers_client(dp)
others.register_handlers_others(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

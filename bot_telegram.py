from aiogram.utils import executor
from create_bot import dp
from handlers import client
from handlers import admin
from handlers import others


async def on_startup(_):
    print("Bot online rejimda ishlamoqda.")

admin.register_handlers_client(dp)
client.register_handlers_client(dp)
others.register_handlers_others(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

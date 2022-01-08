import json
import string
from aiogram import types, Dispatcher
from create_bot import dp


async def bad_word_filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(" ")} \
            .intersection(set(json.load(open("bad_words.json")))) != set():
        await message.reply("Guruhda haqoratli so\'zlar ishlatish ta\'qiqlangan")
        await message.delete()


def register_handlers_others(dispatcher: Dispatcher):
    dispatcher.register_message_handler(bad_word_filter)

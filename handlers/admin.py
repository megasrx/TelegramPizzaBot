from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply("Rasm yuboring")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Endi nomini kiriting")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Mahsulot ta\'rifini kiriting")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply("Narxini kiriting")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    await state.finish()


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(cm_start, commands=['Yuklash'], state=None)
    dispatcher.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dispatcher.register_message_handler(load_name, state=FSMAdmin.name)
    dispatcher.register_message_handler(load_description, state=FSMAdmin.description)
    dispatcher.register_message_handler(load_price, state=FSMAdmin.price)

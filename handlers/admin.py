from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base.sqlite_db import sql_add_command, sql_read2, sql_delete
from keyboards import admin_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(ID, "Yangi mahsulot qo\'shamizmi?", reply_markup=admin_keyboard.button_case_admin)
    await message.delete()


async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply("Rasm yuboring")


async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Yuklash to\'xtatildi.')


async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Endi nomini kiriting")


async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Mahsulot ta\'rifini kiriting")


async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Narxini kiriting")


async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sql_add_command(state)
        await state.finish()


async def del_callback_run(callback_query: types.CallbackQuery):
    await sql_delete(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} o\'chirildi.', show_alert=True)


async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nTa\'vsifi: {ret[2]}\nNarxi: {ret[-1]}')
            await bot.send_message(message.from_user.id, text="^^^", reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'{ret[1]} ni O\'chirish', callback_data=f'del {ret[1]}')))


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(cm_start, commands=['Yuklash'], state=None)
    dispatcher.register_message_handler(cancel_handler, state="*", commands=['Bekor_qilish'])
    dispatcher.register_message_handler(cancel_handler, Text(equals='Bekor_qilish', ignore_case=True), state='*')
    dispatcher.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dispatcher.register_message_handler(load_name, state=FSMAdmin.name)
    dispatcher.register_message_handler(load_description, state=FSMAdmin.description)
    dispatcher.register_message_handler(load_price, state=FSMAdmin.price)
    dispatcher.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dispatcher.register_message_handler(delete_item, lambda message: "O'chirish" in message.text)
    dispatcher.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))

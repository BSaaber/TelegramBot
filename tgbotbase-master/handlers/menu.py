import logging

from aiogram import types

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from dispatcher import dp
import config
from keyboards.inline.main_menu_buttons import menu_keyboard
from keyboards.inline.callback_data import main_menu_callback
from datetime import datetime as dt, date, time
import emoji
from random import randint

grinning_cat = emoji.emojize(":grinning_cat:")  # grinning cat with smiling eyes
grinning_cat_with_smiling_eyes = emoji.emojize(":grinning_cat_with_smiling_eyes:")


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer(text="Привет!", reply_markup=menu_keyboard)


@dp.callback_query_handler(text_contains="main:x_time")
async def x_moment(call: CallbackQuery):
    await call.answer(cache_time=1)
    now = dt.now()
    arrival = dt(2095, 1, 28, 19, 15)
    print(arrival)
    if now > arrival:
        await call.message.answer(text="Событие x произошло!")
    else:
        last_timedelta = arrival - now
        await call.message.answer(text=f"до события x осталось{grinning_cat}:\n{last_timedelta.days} дней"
                                       f"\n{last_timedelta.seconds // 3600} часов"
                                       f"\n{last_timedelta.seconds % 3600 // 60} минут"
                                       f"\n{last_timedelta.seconds % 3600 % 60} секунд")
    logging.info("Просмотрено время до события x")


@dp.callback_query_handler(text_contains="main:y_time")
async def y_moment(call: CallbackQuery):
    await call.answer(cache_time=1)
    now = dt.now()
    birthday = dt(now.year + 50, 2, 13)
    if now > birthday:
        birthday = dt(now.year + 1, 2, 13)
    last_timedelta = birthday - now
    await call.message.answer(
        text=f"до события y осталось{grinning_cat_with_smiling_eyes}:\n{last_timedelta.days} дней"
             f"\n{last_timedelta.seconds // 3600} часов"
             f"\n{last_timedelta.seconds % 3600 // 60} минут"
             f"\n{last_timedelta.seconds % 3600 % 60} секунд")
    logging.info("Просмотрено время до события y")


@dp.callback_query_handler(text_contains="main:kitty_photo")
async def masha_photo(call: CallbackQuery):
    await call.answer(cache_time=1)
    photo = open(f'content/photo/Masha/kitty_photo{randint(1, 7)}.jpg', 'rb')

    await dp.bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    logging.info("Просмотрено фото котёнка")


@dp.callback_query_handler(text_contains="main:tiger_photo")
async def masha_photo(call: CallbackQuery):
    await call.answer(cache_time=1)
    photo = open(f'content/photo/kitties/tiger_photo{randint(1, 3)}.jpg', 'rb')

    await dp.bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo.close()
    logging.info("Просмотрено фото тигра")


@dp.callback_query_handler(text_contains="main:cat_photo")
async def masha_photo(call: CallbackQuery):
    await call.answer(cache_time=1)
    photo = open(f'content/photo/Maxim/cat_photo{randint(1, 3)}.jpg', 'rb')
    await dp.bot.send_photo(chat_id=call.message.chat.id, photo=photo)
    photo.close()
    logging.info("Просмотрено фото кота")


@dp.callback_query_handler(text_contains="main:random_message")
async def love_message(call: CallbackQuery):
    await call.answer(cache_time=1)
    file = open(f"content/text/messages/message{randint(1, 3)}.txt", "r", encoding='utf-8')
    love_text = file.read()
    await call.message.answer(text=love_text)
    file.close()
    logging.info("просмотрено случайное сообщение")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    print(message.text)
    # await message.answer(message.text)
    await message.answer("hello")
    logging.info("написано эхо сообщение")

import sqlite3
import os
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menukeybord import Menu
from loader import dp, db, bot
from states.muzik_state import Muzikstate
from states.video_state import Videostate


@dp.message_handler(text="/start")
@dp.message_handler(state=Muzikstate.muzikstate, text="/start")
@dp.message_handler(state=Videostate.videostate, text="/start")
async def bot_start(message: types.Message, state: FSMContext):
    id = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username
    profil = message.from_user.get_mention()
    # Foydalanuvchini bazaga qo'shamiz
    if username:
        try:
            db.add_user(id=id, name=name, username=username)
        except sqlite3.IntegrityError as err:
            pass
            # await bot.send_message(chat_id=ADMINS[0], text=f"<b>User bazada bor!</b>")
    else:
        try:
            db.add_user(id=id, name=name)
        except sqlite3.IntegrityError as err:
            pass
            #await bot.send_message(chat_id=ADMINS[0], text=f"<b>User bazada bor!</b>")

    xabar=f"Assalomu Alaykum. <b>{name}.</b>\nXush kelibsiz!\nVideodan muzikni olib beraman"
    await message.answer(xabar, reply_markup=Menu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg  = f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg += f"<b>Name:     {name}</b>\n"
    msg += f"<b>Profil:   {profil}</b>\n"
    msg += f"<b>Username: @{username}</b>\n "
    msg += f"<b>Id:       {id}</b>\n\n"
    msg += f"Bazada <b>{count}</b> ta foydalanuvchi bor."
    await bot.send_message(chat_id="5280188027", text=msg)
    await state.finish()


@dp.message_handler(state=Videostate.boshlanishi, text="/start")
async def bot_start(message: types.Message, state: FSMContext):
    text = "Botdan foydalanish uchun /start tugmasini bosing"
    await message.answer(text, reply_markup=Menu)
    id = message.from_user.id
    os.remove(f"video/{id}.mp4")
    await state.finish()

@dp.message_handler(state=Videostate.tugashi, text="/start")
async def bot_start(message: types.Message, state: FSMContext):
    text = "Botdan foydalanish uchun /start tugmasini bosing"
    await message.answer(text, reply_markup=Menu)
    id = message.from_user.id
    os.remove(f"video/{id}.mp4")
    await state.finish()
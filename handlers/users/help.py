from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
import os

from keyboards.default.menukeybord import Menu
from states.muzik_state import Muzikstate
from states.video_state import Videostate


@dp.message_handler(text="/help")
@dp.message_handler(state=Muzikstate.muzikstate, text="/help")
@dp.message_handler(state=Videostate.videostate, text="/help")
async def bot_help(message: types.Message, state: FSMContext):
    text = "Botdan foydalanish uchun /start tugmasini bosing"
    await message.answer(text, reply_markup=Menu)
    await state.finish()


@dp.message_handler(state=Videostate.boshlanishi, text="/help")
async def bot_help(message: types.Message, state: FSMContext):
    text = "Botdan foydalanish uchun /start tugmasini bosing"
    await message.answer(text, reply_markup=Menu)
    id = message.from_user.id
    os.remove(f"video/{id}.mp4")
    await state.finish()

@dp.message_handler(state=Videostate.tugashi, text="/help")
async def bot_help(message: types.Message, state: FSMContext):
    text = "Botdan foydalanish uchun /start tugmasini bosing"
    await message.answer(text, reply_markup=Menu)
    id = message.from_user.id
    os.remove(f"video/{id}.mp4")
    await state.finish()


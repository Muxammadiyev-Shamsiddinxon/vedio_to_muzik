from aiogram.types import InputFile, ContentType
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
import os

from keyboards.default.menukeybord import Menu
from keyboards.default.menugaqaytish import  Menu_qaytish

from handlers.video_editor import muzik_ajrat
from handlers.video_editor import video_cut

from states.muzik_state import Muzikstate
from states.video_state import Videostate

# muzik qirqish jarayoni kodlari
@dp.message_handler(text="Video 🔄 Muzik")
async def bolimga_utish(message: types.Message):
    xabar = f"<b>Video-ni muzikasini qirqib beraman\nVideo Yuboring!  🎦  🔄  🔊</b>"
    await message.answer(xabar, reply_markup=Menu_qaytish)
    await Muzikstate.muzikstate.set()

@dp.message_handler(state=Muzikstate.muzikstate ,content_types=ContentType.VIDEO)
async def muzikni_ajrat(message: types.Message, state: FSMContext):
    id = message.from_user.id
    await message.answer("Tayyorlanmoqda ⏳")
    await message.video.download(f"video/{id}.mp4")
    muzik_ajrat(id)
    muzik = InputFile(path_or_bytesio=f"video/{id}.mp3")
    await message.answer_audio(muzik, caption="@VideoToMuzik_bot")
    await state.finish()
    os.remove(f"video/{id}.mp4")
    os.remove(f"video/{id}.mp3")

@dp.message_handler(text="🔙 Ortga")
async def ortga(message: types.Message):
    await message.answer("Asosiy menu ",reply_markup=Menu)


@dp.message_handler(state=Muzikstate.muzikstate,text="🔙 Ortga")
async def ortga(message: types.Message, state: FSMContext):
    await message.answer("Asosiy menu ",reply_markup=Menu)
    await state.finish()








# Video qirqish jarayoni kodlari
@dp.message_handler(text="Video ✂️")
async def bolimga_utish(message: types.Message):
    xabar = f"<b>Video-ni uzini qirqib beraman\nVideo Yuboring!  🎦  ✂️</b>"
    await message.answer(xabar, reply_markup=Menu_qaytish)
    await Videostate.videostate.set()

@dp.message_handler(state=Videostate.videostate ,content_types=ContentType.VIDEO)
async def video_yuklash(message: types.Message):
    id = message.from_user.id
    await message.video.download(f"video/{id}.mp4")
    xabar = f"Videoni qaysi oraliqlari qirqilishi kerak yuboring\n\n"
    xabar += f"<b>NAMUNALAR:\n1)    1 2\n2)    5 10\n3)    40 50</b>\n\n"
    xabar += f"Shunchaki 2 ta raqamni yani boshlanishi va tugashini kiritsangiz boldi"
    await message.answer(xabar)
    await Videostate.boshlanishi.set()

@dp.message_handler(state=Videostate.videostate,text="🔙 Ortga")
async def ortga(message: types.Message, state: FSMContext):
    await message.answer("Asosiy menu ",reply_markup=Menu)
    await state.finish()


@dp.message_handler(state=Videostate.boshlanishi,text="🔙 Ortga")
async def ortga(message: types.Message, state: FSMContext):
    await message.answer("Asosiy menu ",reply_markup=Menu)
    id = message.from_user.id
    os.remove(f"video/{id}.mp4")
    await state.finish()


@dp.message_handler(state=Videostate.boshlanishi)
async def muzikni_ajrat(message: types.Message, state: FSMContext):
    try:
        a, b = list(map(int, message.text.split()))
        int(a)
        int(b)
        time1=int(a)
        time2=int(b)
        id = message.from_user.id
        video_cut(id,time1,time2)
        video = InputFile(path_or_bytesio=f"video/video{id}.mp4")
        await message.answer_video(video, caption="@VideoToMuzik_bot", reply_markup=Menu)
        os.remove(f"video/{id}.mp4")
        os.remove(f"video/video{id}.mp4")
        await state.finish()
    except:
        xabar = f"Raqam yuboring!\n\n"
        xabar += f"<b>NAMUNALAR:\n1)    1 2\n2)    5 10\n3)    40 50</b>\n\n"
        xabar += f"Shunchaki 2 ta raqamni yani bolanishi va tugashini kiritsangiz bo'ldi"
        await message.answer(xabar)





@dp.message_handler(state=Muzikstate.muzikstate)
@dp.message_handler(state=Muzikstate.muzikstate, content_types=ContentType.PHOTO)
@dp.message_handler(state=Muzikstate.muzikstate, content_types=ContentType.VOICE)
@dp.message_handler(state=Muzikstate.muzikstate, content_types=ContentType.AUDIO)
async def holat(message: types.Message):
    xabar = f"<b>Iltimos video yuboring!</b>"
    await message.answer(xabar)

@dp.message_handler()
@dp.message_handler(content_types=ContentType.PHOTO)
@dp.message_handler(content_types=ContentType.VOICE)
@dp.message_handler(content_types=ContentType.AUDIO)
async def holat(message: types.Message):
    xabar = f"<b>Iltimos men sizni tushunmayapman\nmenga bo'limlar orqali murojat qiling!</b>\n"
    await message.answer(xabar, reply_markup=Menu)
# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import VoiceAktyorState



@dp.callback_query_handler(lambda c: c.data.startswith("completed_voice_"))
async def complated(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(texts.VOICE_AKTYOR_FILE_SEND)
    
    await VoiceAktyorState.file.set()


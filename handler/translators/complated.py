# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import Translators



@dp.callback_query_handler(lambda c: c.data.startswith("completed_"))
async def complated(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(texts.TRANSLATORS_FILE_SEND)
    
    await Translators.file.set()


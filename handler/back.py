# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from state import NewAnimeState



@dp.callback_query_handler(lambda call: call.data == 'go_back', state='*')
async def back_handler(callback: CallbackQuery, state: FSMContext):
    
    await callback.message.delete()
    
    await callback.message.answer(texts.SHIKIMORE_URL, reply_markup=buttons.BACK)
    await NewAnimeState.shikimore_url.set()
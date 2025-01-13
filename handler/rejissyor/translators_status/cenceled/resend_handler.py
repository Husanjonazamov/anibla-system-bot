# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import TranslatorCencelledState




@dp.callback_query_handler(lambda call: call.data.startswith('resend_'), state='*')
async def resend_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(texts.TRANSLATORS_FILE_SEND)
    data = callback.data.split("_")
    rejissyor_id = int(data[1])  
    translator_id = int(data[2]) 
    
    await callback.message.delete()
    
    await state.update_data({"rejissyor_id":rejissyor_id})
    
    await TranslatorCencelledState.file.set()
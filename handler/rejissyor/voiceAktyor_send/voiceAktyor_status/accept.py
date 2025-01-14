# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorTimerState



@dp.callback_query_handler(lambda call: call.data.startswith('voice_work_accept_'), state='*')
async def translator_accept_status(callback: CallbackQuery, state: FSMContext):
    callback_data = callback.data.split("_")  
    rejissyor_id = int(callback_data[3])
    voice_aktyor_id = int(callback_data[4]) 
    
    
    await state.update_data({'rejissyor_id': rejissyor_id})
    
    await bot.send_message(
        chat_id=voice_aktyor_id,
        text=texts.SUCCES_VOICE_AKTYOR_FILE
    )
    
    await callback.message.edit_reply_markup(reply_markup=buttons.update_translators_accept_button())
    
    await callback.message.answer(texts.TIMER_SOURCE_FILE)
    await RejissyorTimerState.file.set()
    
    
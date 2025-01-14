# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import VoiceActorState



@dp.callback_query_handler(lambda call: call.data.startswith('translator_work_accept_'), state='*')
async def translator_accept_status(callback: CallbackQuery, state: FSMContext):
    callback_data = callback.data.split("_")  
    rejissyor_id = int(callback_data[3])
    translator_id = int(callback_data[4])  
    
    await state.update_data({'rejissyor_id': rejissyor_id})
    
    await bot.send_message(
        chat_id=translator_id,
        text=texts.SUCCES_TRANSLATOR_FILE
    )
    
    await callback.message.edit_reply_markup(reply_markup=buttons.update_translators_accept_button())
    
    await callback.message.answer(texts.VOICE_SOURCE_FILE)
    await VoiceActorState.file.set()
    
    
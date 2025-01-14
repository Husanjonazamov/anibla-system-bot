# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorState
from services.services import getTranslatorList



@dp.callback_query_handler(lambda c: c.data.startswith("submit_voice_"), state='*')
async def submit_voice_handler(callback_query: CallbackQuery, state: FSMContext):
    
    data = await state.get_data()
    selected_voice = data.get("selected_voice", [])
    selected_files = data.get("files", [])
    rejissyor_id = data.get('rejissyor_id')  
    
    
    if selected_voice and selected_files:
        for voice_aktyor_id in selected_voice:
            for file in selected_files:
                keyboard = buttons.create_accept_voice_button(voice_aktyor_id, rejissyor_id)
                
                await bot.send_document(
                    chat_id=voice_aktyor_id,
                    document=file['file_id'],
                    caption=texts.WORKER_NOTIFICATION_TEXT,
                    reply_markup=keyboard
                )
        await callback_query.message.delete()
        await callback_query.message.answer(texts.SUCCESS_TRANSLATORS)
    else:
        await callback_query.answer(texts.NOT_VOICE_AKTYOR)
    
    await state.finish()

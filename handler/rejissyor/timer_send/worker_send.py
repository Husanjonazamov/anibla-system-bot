# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorState
from services.services import getTranslatorList



@dp.callback_query_handler(lambda c: c.data.startswith("submit_timer_"), state='*')
async def submit_timer_handler(callback_query: CallbackQuery, state: FSMContext):
    
    data = await state.get_data()
    selected_timer = data.get("selected_timer", [])
    selected_files = data.get("files", [])
    rejissyor_id = data.get('rejissyor_id')  
    
    
    if selected_timer and selected_files:
        for timer_id in selected_timer:
            for file in selected_files:
                keyboard = buttons.create_accept_timer_button(timer_id, rejissyor_id)
                
                await bot.send_document(
                    chat_id=timer_id,
                    document=file['file_id'],
                    caption=texts.WORKER_NOTIFICATION_TEXT,
                    reply_markup=keyboard
                )
        await callback_query.message.delete()
        await callback_query.message.answer(texts.SUCCES_TIMER)
    else:
        await callback_query.answer(texts.NOT_TIMER)
    
    await state.finish()

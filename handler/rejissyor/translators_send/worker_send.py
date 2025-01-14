# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorState
from services.services import getTranslatorList



@dp.callback_query_handler(lambda c: c.data.startswith("submit_translators_"), state='*')
async def submit_translators_handler(callback_query: CallbackQuery, state: FSMContext):
    
    
    data = await state.get_data()
    selected_translators = data.get("selected_translators", [])
    selected_files = data.get("files", [])
    rejissyor_id = data.get('rejissyor_id')  
    print(rejissyor_id)
    
    if selected_translators and selected_files:
        for translator_id in selected_translators:
            print(translator_id)
            for file in selected_files:
                keyboard = buttons.create_accept_translator_button(translator_id, rejissyor_id)
                
                await bot.send_document(
                    chat_id=translator_id,
                    document=file['file_id'],
                    caption=texts.WORKER_NOTIFICATION_TEXT,
                    reply_markup=keyboard
                )
        await callback_query.message.delete()
        await callback_query.message.answer(texts.SUCCESS_VOICE_AKTYOR)
    else:
        await callback_query.answer(texts.NOT_TRANSLATORS)
    
    await state.finish()

# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorState
from services.services import getTranslatorList




@dp.callback_query_handler(lambda c: c.data == "submit_translators", state=RejissyorState.worker_send)
async def submit_translators(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    selected_translators = data.get("selected_translators", [])
    selected_files = data.get("files", [])
    
    rejissyor_id = data.get('rejissyor_id')
    
    
    if selected_translators and selected_files:
        for translator_id in selected_translators:
            for file in selected_files:
                keyboard = buttons.create_accept_translator_button(translator_id, rejissyor_id)
                
                await bot.send_document(
                    chat_id=translator_id,
                    document=file['file_id'],
                    caption=texts.TRANSLATOR_NOTIFICATION_TEXT,
                    reply_markup=keyboard
                )
        await callback_query.answer(texts.SUCCESS_TRANSLATORS)
    else:
        await callback_query.answer(texts.NOT_TRANSLATORS)
    
    await state.finish()





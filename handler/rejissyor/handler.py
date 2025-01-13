# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorState



@dp.callback_query_handler(lambda call: call.data.startswith("accept_rejissor"), state='*')
async def accept_rejissor_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(texts.REJISSYOR_ACCEPT)
    callback_data = callback_query.data.split("_")
    rejissyor_id = callback_data[1].split(':')[1] 
    
    
    await state.update_data({
        'rejissyor_id':rejissyor_id
    })
    
    await callback_query.message.answer(texts.REJISSOR_SOURCE_FILE, reply_markup=buttons.create_cancel_button())
    await callback_query.message.edit_reply_markup(reply_markup=buttons.create_accept_button(rejissyor_id, accepted=True))
    
    await RejissyorState.file.set()
    
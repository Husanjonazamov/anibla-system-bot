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
    
    await callback_query.message.answer(texts.REJISSOR_SOURCE_FILE, reply_markup=buttons.create_cancel_button())
    
    await RejissyorState.file.set()
    
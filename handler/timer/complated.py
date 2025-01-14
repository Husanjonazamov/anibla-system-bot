# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import TimerState



@dp.callback_query_handler(lambda c: c.data.startswith("completed_timer_"))
async def complated(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(texts.TIMER_FILE_SEND)
    
    await TimerState.file.set()


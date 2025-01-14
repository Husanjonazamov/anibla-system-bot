# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import TimerCenceledState




@dp.callback_query_handler(lambda call: call.data.startswith('re_sendtimer_'), state='*')
async def resend_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(texts.TIMER_FILE_SEND)
    data = callback.data.split("_")
    rejissyor_id = int(data[2])  
    timer_id = int(data[3]) 
    
    await callback.message.delete()
    
    await state.update_data({"rejissyor_id":rejissyor_id})
    
    await TimerCenceledState.file.set()
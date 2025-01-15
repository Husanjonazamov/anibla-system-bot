# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons



@dp.callback_query_handler(lambda call: call.data.startswith('timer_work_accept_'))
async def accept_anime_handler(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split('_')
    timer_id = int(data[4]) 
    await callback.message.answer(texts.SUCCESS_ANIME)
    
    await bot.send_message(
        chat_id=timer_id,
        text=texts.SUCCESS_ANIME_WORKER
    )
# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons



@dp.callback_query_handler(lambda c: c.data.startswith("accept_timer_"), state='*')
async def accept_file(callback_query: CallbackQuery, state: FSMContext):
    data = callback_query.data.split("_")
    
    timer_id = int(data[2])
    rejissyor_id = int(data[3])
    
    await state.update_data({'rejissyor_id': rejissyor_id})

    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,   
        reply_markup=buttons.create_completed_timer_button(timer_id)
    )   

    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=texts.TIMER_ACCEPT
    )
# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons



@dp.callback_query_handler(lambda c: c.data.startswith("accept_voice_aktyor_"), state='*')
async def accept_file(callback_query: CallbackQuery, state: FSMContext):
    data = callback_query.data.split("_")
    voice_aktyor_id = int(data[3])
    print(voice_aktyor_id)
    rejissyor_id = int(data[4])
    
    await state.update_data({'rejissyor_id': rejissyor_id})

    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,   
        reply_markup=buttons.create_completed_voice_aktyor_button(voice_aktyor_id)
    )   

    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=texts.VOICE_AKTYOR_ACCEPT
    )
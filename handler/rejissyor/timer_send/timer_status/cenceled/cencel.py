# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import TranslatorCencelledState




@dp.callback_query_handler(lambda callback: callback.data.startswith('retimer_'), state='*')
async def translator_cencel(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split("_")

    rejissyor_id = int(data[1])   
    timer_id = int(data[2])  
    await state.update_data({'rejissyor_id': rejissyor_id})
    
    await bot.send_message(
        chat_id=timer_id,
        text=texts.CANCELLED_TIMER_SEND,
        reply_markup=buttons.timer_resend_file_button(rejissyor_id, timer_id)
    )

    await callback.message.edit_reply_markup(reply_markup=buttons.update_translators_cencelled_button())

    await callback.answer(texts.CANCELLED_TIMER_FILE)

        


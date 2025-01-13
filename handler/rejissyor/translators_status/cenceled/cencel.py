# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import TranslatorCencelledState




@dp.callback_query_handler(lambda callback: callback.data.startswith('reject_'), state='*')
async def translator_cencel(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split("_")

    rejissyor_id = int(data[1])   
    translator_id = int(data[2])  
    await state.update_data({'rejissyor_id': rejissyor_id})
    
    await bot.send_message(
        chat_id=translator_id,
        text=texts.CANCELLED_TRANSLATOR_SEND,
        reply_markup=buttons.create_resend_file_button(rejissyor_id, translator_id)
    )
    await TranslatorCencelledState.file.set()

    await callback.answer(texts.CANCELLED)

        


# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import TimerCenceledState

@dp.message_handler(content_types=['text'], state=TimerCenceledState.feedback)
async def timer_feedback(message: Message, state: FSMContext):
    feedback = message.text
    data = await state.get_data()
    file = data.get('file_id')
    rejissyor_id = data.get('rejissyor_id')
    
    timer_id = message.from_user.id
    
    await bot.send_document(
        chat_id=rejissyor_id,
        document=file,
        caption=feedback,
        reply_markup=buttons.create_accept_or_reject_button(rejissyor_id, timer_id)
    )
    
    await message.answer(texts.TIMER_WORK_SEND)
    
    await state.finish()
    
    
    
    
    




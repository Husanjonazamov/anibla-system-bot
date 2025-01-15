# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import TimerState
from services.services import getUser


@dp.message_handler(content_types=['text'], state=TimerState.feedback)
async def voice_feedback(message: Message, state: FSMContext):
    feedback = message.text
    data = await state.get_data()
    file = data.get('file_id')
    rejissyor_id = data.get('rejissyor_id')
    
    timer_id = message.from_user.id
    
    user = getUser(timer_id)
    
    firstname = user['results'][0]['first_name']
    stage_name = user['results'][0]['stage_name']
    
    await bot.send_document(
        chat_id=rejissyor_id,
        document=file,
        caption=texts.timer_text(
                firstname=firstname,
                stage_name=stage_name,
                feedback=feedback
            ),
        reply_markup=buttons.accept_or_reject_timer_button(rejissyor_id, timer_id)
    )
    
    await message.answer(texts.TIMER_WORK_SEND)
    
    await state.finish()
    
    
    
    
    




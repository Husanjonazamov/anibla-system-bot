# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kod import
from loader import dp, bot
from utils import texts, buttons
from state import TimerState





@dp.message_handler(content_types=['document'], state=TimerState.file)
async def timer_file_handler(message: Message, state: FSMContext):
    document = message.document


    file_id = document.file_id
    file_name = document.file_name

    await state.update_data(
        file_id=file_id,
        file_name=file_name,
        user_id=message.from_user.id
    )
    
    await message.answer(texts.TIMER_FEEDBACK, reply_markup=buttons.BACK)
    await TimerState.feedback.set()
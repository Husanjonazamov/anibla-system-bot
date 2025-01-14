# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kod import
from loader import dp, bot
from utils import texts, buttons
from state import TimerState





@dp.message_handler(content_types=["document", "video", "voice", "audio"], state=TimerState.file)
async def timer_file_handler(message: Message, state: FSMContext):
    if message.video:
        file_id = message.video.file_id
    elif message.voice:
        file_id = message.voice.file_id
    elif message.audio:
        file_id = message.audio.file_id
    else:
        file_id = message.document.file_id

    await state.update_data(
        file_id=file_id,
        user_id=message.from_user.id
    )
    
    await message.answer(texts.TIMER_FEEDBACK, reply_markup=buttons.BACK)
    await TimerState.feedback.set()
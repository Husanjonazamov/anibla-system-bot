# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorTimerState
from services.services import getTimerList



@dp.message_handler(content_types=["document", "video", "voice", "audio"], state=RejissyorTimerState.file)
async def process_file(message: Message, state: FSMContext):
    if message.video:
        file_id = message.video.file_id
    elif message.voice:
        file_id = message.voice.file_id
    elif message.audio:
        file_id = message.audio.file_id
    else:
        file_id = message.document.file_id
    
    user_data = await state.get_data()
    files = user_data.get('files', [])
    
    if files is None:
        files = []
    
    files.append({'file_id': file_id})
    
    await state.update_data(files=files)    
        
    timer = getTimerList()

    await message.answer(
        texts.TIMER_WORKER_LIST, 
        reply_markup=buttons.create_timer_buttons(timer, [])
    )
    
    await RejissyorTimerState.timer_worker.set()

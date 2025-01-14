# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import VoiceActorState
from services.services import getVoiceAktyorList



@dp.message_handler(content_types=["document"], state=VoiceActorState.file)
async def process_file(message: Message, state: FSMContext):
    file_id = message.document.file_id
    file_name = message.document.file_name
    
    user_data = await state.get_data()
    files = user_data.get('files', [])
    
    if files is None:
        files = []
    
    files.append({'file_id': file_id, 'file_name': file_name})
    
    await state.update_data(files=files)
    
    voice_aktyor = getVoiceAktyorList()

    await message.answer(
        texts.VOICE_WORKER_LIST, 
        reply_markup=buttons.create_voice_aktyor_buttons(voice_aktyor, [])
    )
    
    await VoiceActorState.voice_worker.set()

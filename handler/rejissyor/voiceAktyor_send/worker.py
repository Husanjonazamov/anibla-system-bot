# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejisyorVoiceAktyorState
from services.services import getVoiceAktyorList



@dp.callback_query_handler(lambda c: c.data.startswith("select_voice_"), state=RejisyorVoiceAktyorState.voice_worker)
async def select_voice(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    selected_voice_id = callback_query.data.split("_")[2]

    data = await state.get_data()
    selected_voice = data.get("selected_voice", [])
    
    if selected_voice_id not in selected_voice:
        selected_voice.append(selected_voice_id)
    else:
        selected_voice.remove(selected_voice_id)
    
    await state.update_data(selected_voice=selected_voice)
    
    voice_aktyor = getVoiceAktyorList()
    
    await callback_query.message.edit_reply_markup(
        reply_markup=buttons.create_voice_aktyor_buttons(voice_aktyor, selected_voice)
    )
    
    selected_names = [t['first_name'] for t in voice_aktyor if str(t['user_id']) in selected_voice]
    await callback_query.answer(f"Tanlangan Ovoz aktyorlari: {', '.join(selected_names)}")


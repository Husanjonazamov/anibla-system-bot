# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorState
from services.services import getTranslatorList



@dp.callback_query_handler(lambda c: c.data.startswith("select_translator_"), state=RejissyorState.worker)
async def select_translator(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    selected_translator_id = callback_query.data.split("_")[2]

    data = await state.get_data()
    selected_translators = data.get("selected_translators", [])
    
    if selected_translator_id not in selected_translators:
        selected_translators.append(selected_translator_id)
    else:
        selected_translators.remove(selected_translator_id)
    
    await state.update_data(selected_translators=selected_translators)
    
    translators = getTranslatorList()
    
    await callback_query.message.edit_reply_markup(
        reply_markup=buttons.create_translator_buttons(translators, selected_translators)
    )
    
    selected_names = [t['first_name'] for t in translators if str(t['user_id']) in selected_translators]
    await callback_query.answer(f"Tanlangan tarjimonlar: {', '.join(selected_names)}")


    # await RejissyorState.worker_send.set()
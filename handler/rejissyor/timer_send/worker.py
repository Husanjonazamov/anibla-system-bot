# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import RejissyorTimerState
from services.services import getTimerList



@dp.callback_query_handler(lambda c: c.data.startswith("select_timer_"), state=RejissyorTimerState.timer_worker)
async def select_timer(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    selected_timer_id = callback_query.data.split("_")[2]

    data = await state.get_data()
    selected_timer = data.get("selected_timer", [])
    
    if selected_timer_id not in selected_timer:
        selected_timer.append(selected_timer_id)
    else:
        selected_timer.remove(selected_timer_id)
    
    await state.update_data(selected_timer=selected_timer)
    
    timer = getTimerList()
    
    await callback_query.message.edit_reply_markup(
        reply_markup=buttons.create_timer_buttons(timer, selected_timer)
    )
    
    selected_names = [t['first_name'] for t in timer if str(t['user_id']) in selected_timer]
    await callback_query.answer(f"Tanlangan Timerlar: {', '.join(selected_names)}")


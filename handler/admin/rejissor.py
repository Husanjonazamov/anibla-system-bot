# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from state import NewAnimeState
from services.services import getUser
from utils import texts, buttons



@dp.callback_query_handler(lambda call: call.data.startswith('user_id_'), state=NewAnimeState.rejissor)
async def rejissyor_handler(callback: CallbackQuery, state: FSMContext):
    
    rejissyor = callback.data.split('_')[2] 
    
    await callback.message.delete()
    
    await state.update_data(
        {'rejissyor': rejissyor}
    )
    
    user_id = rejissyor
    user = getUser(user_id)
    first_name = user['results'][0]['first_name']

    data = await state.get_data()
    name = data.get('name')
    uz_name = data.get('uz_name')
    shikimore_url = data.get('shikimore_url')    
    
    
    caption = texts.addAnime(
        name=name,
        uz_name=uz_name,
        shikimore_url=shikimore_url,
        first_name=first_name
    )
    
    await callback.message.answer(
        text=caption,    
        reply_markup=buttons.ADMIN_CHECK
    )
    
    await NewAnimeState.check.set()
    
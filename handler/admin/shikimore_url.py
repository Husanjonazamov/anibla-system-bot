from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import texts, buttons
from state import NewAnimeState
from services.services import getRejissyorList




@dp.message_handler(content_types=['text'], state=NewAnimeState.shikimore_url)
async def anime_shikimore_url(message: Message, state: FSMContext):
    
    shikimore_url = message.text
    
    if shikimore_url == buttons.BASE_BACK:
        await message.answer(texts.ANIME_UZNAME, reply_markup=buttons.BACK)
        await NewAnimeState.uz_name.set()
    else:
        await state.update_data({
            'shikimore_url': shikimore_url
            })
        
        rejissyor = getRejissyorList()
        
        await message.answer(texts.SELECT_REJISSYOR, reply_markup=buttons.create_inline_buttons(rejissyor))
        
        await NewAnimeState.rejissor.set()

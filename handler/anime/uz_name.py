# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from state import NewAnime
from handler.anime.handler import newanime_handler


@dp.message_handler(content_types=['text'], state=NewAnime.uz_name)
async def anime_uzname(message: Message, state: FSMContext):
    
    uz_name = message.text
    
    if uz_name == buttons.BASE_BACK:
        await newanime_handler(message, state)
    else:
        await state.update_data({
            'uz_name': uz_name
            })
        
        await message.answer(texts.SHIKIMORE_URL, reply_markup=buttons.BACK)
        
        await NewAnime.shikimore_url.set()
    
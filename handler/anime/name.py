# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from state import NewAnime
from handler.start import start_handler

@dp.message_handler(content_types=['text'], state=NewAnime.name)
async def anime_name(message: Message, state: FSMContext):
    
    name = message.text
    if name == buttons.BASE_BACK:
        await start_handler(message, state)
    else:
        await state.update_data({
            'name': name
        })
        
        await message.answer(texts.ANIME_UZNAME, reply_markup=buttons.BACK)
        
        await NewAnime.uz_name.set()
        
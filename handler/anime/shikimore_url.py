from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import texts, buttons
from state import NewAnime
from services.services import getRejissyor


@dp.message_handler(content_types=['text'], state=NewAnime.shikimore_url)
async def anime_shikimore_url(message: Message, state: FSMContext):
    
    shikimore_url = message.text
    
    await state.update_data({
        'shikimore_url': shikimore_url
        })
    
    rejissyor = getRejissyor()
    
    await message.answer(texts.SHIKIMORE_URL, reply_markup=buttons.create_inline_buttons(rejissyor))
    
    await NewAnime.rejissor.set()

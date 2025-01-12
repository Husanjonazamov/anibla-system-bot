# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from state import NewAnimeState


@dp.message_handler(lambda message: message.text.startswith(buttons.NEW_ANIME_BUTTON), state='*')
async def newanime_handler(message: Message, state: FSMContext):
    
    await message.answer(texts.ANIME_NAME, reply_markup=buttons.BACK)
    
    await NewAnimeState.name.set()
    
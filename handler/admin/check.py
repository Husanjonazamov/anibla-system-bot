# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import NewAnime
from services.services import createAnime


@dp.message_handler(lambda message: message.text.startswith(buttons.CHECK), state=NewAnime.check)
async def check_handler(message: Message, state: FSMContext):
    
    data = await state.get_data()
    rejissyor = data.get('rejissyor')
    name = data.get('name')
    uz_name = data.get('uz_name')
    shikimore_url = data.get('shikimore_url')
    
    caption = texts.rejissyor_nontification(
        name=name,
        uz_name=uz_name,
        shikimore_url=shikimore_url
    )
    await bot.send_message(
        chat_id=rejissyor,
        text=caption, 
        reply_markup=buttons.create_accept_button()
    )
    
    
    anime = ({
        'name': name,
        'uz_name': uz_name,
        'shikimore_url': shikimore_url,
        'rejissyor': rejissyor
    })    
    
    createAnime(anime)
    
    await message.answer(texts.SUCESS_ADMIN, reply_markup=buttons.ADMINPANEL)
    
    
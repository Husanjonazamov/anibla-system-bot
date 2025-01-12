# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from state import NewAnime



@dp.message_handler(lambda message: message.text.startswith(buttons.CHECK), state=NewAnime.check)
async def check_handler(message: Message, state: FSMContext):
    
    data = await state.get_data()
    rejissyor_id = data.get('rejissyor')
    name = data.get('name')
    uz_name = data.get('uz_name')
    shikimore_url = data.get('shikimore_url')
    
    caption = texts.rejissyor_nontification(
        name=name,
        uz_name=uz_name,
        shikimore_url=shikimore_url
    )
    print(rejissyor_id)
    await bot.send_message(
        chat_id=rejissyor_id,
        text=caption
    )
    await message.answer('yahshi')
    
# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from handler.start import start_handler



@dp.message_handler(lambda message: message.text.startswith(buttons.CENCEL), state='*')
async def cencel_handler(message: Message, state: FSMContext):
    
    await start_handler(message, state)
    
    
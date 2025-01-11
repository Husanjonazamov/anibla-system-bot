# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services.services import getUser


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    """
    botni asosiy /start funksiyasi
    """
    firstname = message.from_user.first_name
    user_id = message.from_user.id
    
    user = getUser(user_id)
    role = user['results'][0]['role']

    if role == 'admin':
        await message.answer(texts.START.format(firstname), reply_markup=buttons.ADMINPANEL)
    else:
        await message.answer(texts.START.format(firstname))
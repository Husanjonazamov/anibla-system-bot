# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons



@dp.callback_query_handler(lambda call: call.data.startswith('accept_'))
async def translator_accept_status(callback: CallbackQuery, state: FSMContext):
    pass
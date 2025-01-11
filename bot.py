# aiogram import
from aiogram import executor

# kode import
from loader import bot, dp
from utils.env import ADMIN

import handler


async def on_startup(dp):
    """
    Botni asosiy ishga tushiradigan file
    """
    
    await bot.send_message(ADMIN, 'bot ishga tushdi')
    
    
executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
# aiogram import
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# add import
from utils.env import BOT_TOKEN
import logging

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot, storage=storage)




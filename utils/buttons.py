from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



NEW_ANIME_BUTTON = "Yangi anime qo'shish" 


ADMINPANEL = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=NEW_ANIME_BUTTON)
        ]
    ],
    resize_keyboard=True
)


BASE_BACK = "🔙 Ortga"

BACK = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)





def create_inline_buttons(user_data):
    directors = [user for user in user_data if user['role'] == "rejissyor"]
    
    keyboard = [
        [InlineKeyboardButton(user['first_name'], callback_data=user['user_id'])] for user in directors
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
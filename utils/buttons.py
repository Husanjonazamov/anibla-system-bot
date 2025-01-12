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


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_inline_buttons(directors):
    keyboard = InlineKeyboardMarkup(row_width=1) 
    for director in directors:
        
        callback_data = f"user_id_{director.get('user_id')}"
        
        button = InlineKeyboardButton(
            text=director.get("first_name"),  
            callback_data=callback_data
        )

        keyboard.add(button)
    
    back_button = InlineKeyboardButton(
        text="🔙 Orqaga",  
        callback_data="go_back"  
    )
    
    keyboard.add(back_button)  
    return keyboard




CHECK = 'Yuborish'
CENCEL = 'Bekor qilish'


ADMIN_CHECK = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CHECK),
        ],
        [
            KeyboardButton(text=CENCEL)
        ]
    ],
    resize_keyboard=True
)
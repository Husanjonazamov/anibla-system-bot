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

def create_accept_button(rejissyor):
    keyboard = InlineKeyboardMarkup(row_width=1)
    
    accept_button = InlineKeyboardButton(
        text="✅ Qabul qilish",
        callback_data=f"accept_rejissor:{rejissyor}" 
    )
    keyboard.add(accept_button)
    
    return keyboard


REJISSYOR_FILE_CENCEL = "❌ Bekor qilish"

def create_cancel_button():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    cancel_button = KeyboardButton(text=REJISSYOR_FILE_CENCEL)
    keyboard.add(cancel_button)
    
    return keyboard



def create_translator_buttons(translators, selected_translators):
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    for translator in translators:
        translator_id = translator.get("user_id")
        first_name = translator.get("first_name")
        
        if translator_id in selected_translators:
            button_text = f"✅ {first_name}"
        else:
            button_text = first_name
        
        button = InlineKeyboardButton(
            text=button_text,  
            callback_data=f"select_translator_{translator_id}"  
        )
        keyboard.add(button)

    accept_button = InlineKeyboardButton(
        text="📤 Yuborish",  
        callback_data="submit_translators_"  
    )
    keyboard.add(accept_button)
    
    return keyboard



def create_accept_translator_button(translator_id: int, rejissyor_id: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Qabul qilish",
            callback_data=f"accept__translator_{translator_id}_{rejissyor_id}" 
        )
    )
    return keyboard



def create_completed_button(translator_id: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Bajarildi",
            callback_data=f"completed_{translator_id}"
        )
    )
    return keyboard



def create_accept_or_reject_button(translator_id: int, rejissyor_id: int):
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text="✅Qabul qilaman",
            callback_data=f"translator_work_accept{translator_id}_{rejissyor_id}"
        )
    )
    
    keyboard.add(
        InlineKeyboardButton(
            text="❌ Qayta yuborish",
            callback_data=f"reject_{translator_id}_{rejissyor_id}"
        )
    )
    
    return keyboard



def create_resend_file_button(rejissyor_id: int, translator_id: int):
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text="📤 Yana faylni yuborish",
            callback_data=f"resend_{rejissyor_id}_{translator_id}"
        )
    )
    
    return keyboard
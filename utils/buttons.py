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

def create_accept_button(rejissyor, accepted=False):
    keyboard = InlineKeyboardMarkup(row_width=1)
    
    if accepted:
        accept_button = InlineKeyboardButton(
            text="📥 Qabul qilingan", 
            callback_data="accepted_rejissyor_button"  
        )
    else:
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



def create_completed_translator_button(translator_id: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Bajarildi",
            callback_data=f"completed_translator_{translator_id}"
        )
    )
    return keyboard



def create_accept_or_reject_button(translator_id: int, rejissyor_id: int):
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text="✅Qabul qilaman",
            callback_data=f"translator_work_accept_{translator_id}_{rejissyor_id}"
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




def update_translators_cencelled_button():
    new_keyboard = InlineKeyboardMarkup()
    new_keyboard.add(
        InlineKeyboardButton(
            text="❌ Bekor qilingan", 
            callback_data="update_translator_cancelled"  
        )
    )
    
    return new_keyboard


def update_translators_accept_button():
    update_button = InlineKeyboardMarkup()
    update_button.add(
        InlineKeyboardButton(
            text="📥 Qabul qilingan", 
            callback_data="update_translator_accept"  
        )
    )
    
    return update_button




def create_voice_aktyor_buttons(voice_aktyor, selected_voice):
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    for translator in voice_aktyor:
        translator_id = translator.get("user_id")
        first_name = translator.get("first_name")
        
        if translator_id in selected_voice:
            button_text = f"✅ {first_name}"
        else:
            button_text = first_name
        
        button = InlineKeyboardButton(
            text=button_text,  
            callback_data=f"select_voice_{translator_id}"  
        )
        keyboard.add(button)

    accept_button = InlineKeyboardButton(
        text="📤 Yuborish",  
        callback_data="submit_voice_"  
    )
    keyboard.add(accept_button)
    
    return keyboard





def create_accept_voice_button(voice_aktyor_id: int, rejissyor_id: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Qabul qilish",
            callback_data=f"accept_voice_aktyor_{voice_aktyor_id}_{rejissyor_id}" 
        )
    )
    return keyboard


def create_completed_voice_aktyor_button(voice_aktyor_id: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Bajarildi",
            callback_data=f"completed_voice_{voice_aktyor_id}"
        )
    )
    return keyboard




def create_accept_or_reject_voice_button(voice_aktyor_id: int, rejissyor_id: int):
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text="✅Qabul qilaman",
            callback_data=f"voice_work_accept_{voice_aktyor_id}_{rejissyor_id}"
        )
    )
    
    keyboard.add(
        InlineKeyboardButton(
            text="❌ Qayta yuborish",
            callback_data=f"revoice_aktyor_{voice_aktyor_id}_{rejissyor_id}"
        )
    )
    
    return keyboard



def voice_resend_file_button(rejissyor_id: int, voice_aktyor_id: int):
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text="📤 Yana faylni yuborish",
            callback_data=f"resend_voice_{rejissyor_id}_{voice_aktyor_id}"
        )
    )
    
    return keyboard





def create_timer_buttons(timer, selected_voice):
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    for timer_info in timer:
        timer_id = timer_info.get("user_id")
        first_name = timer_info.get("first_name")
        
        if timer_id in selected_voice:
            button_text = f"✅ {first_name}"
        else:
            button_text = first_name
        
        button = InlineKeyboardButton(
            text=button_text,  
            callback_data=f"select_timer_{timer_id}"  
        )
        keyboard.add(button)

    accept_button = InlineKeyboardButton(
        text="📤 Yuborish",  
        callback_data="submit_timer_"  
    )
    keyboard.add(accept_button)
    
    return keyboard



def create_accept_timer_button(timer_id: int, rejissyor_id: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Qabul qilish",
            callback_data=f"accept_timer_{timer_id}_{rejissyor_id}" 
        )
    )
    return keyboard



def create_completed_timer_button(timer_id: int):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Bajarildi",
            callback_data=f"completed_timer_{timer_id}"
        )
    )
    return keyboard





def accept_or_reject_timer_button(timer_id: int, rejissyor_id: int):
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text="✅Qabul qilaman",
            callback_data=f"timer_work_accept_{timer_id}_{rejissyor_id}"
        )
    )
    
    keyboard.add(
        InlineKeyboardButton(
            text="❌ Qayta yuborish",
            callback_data=f"retimer_{timer_id}_{rejissyor_id}"
        )
    )
    
    return keyboard



def timer_resend_file_button(rejissyor_id: int, timer_id: int):
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text="📤 Yana faylni yuborish",
            callback_data=f"re_sendtimer_{rejissyor_id}_{timer_id}"
        )
    )
    
    return keyboard
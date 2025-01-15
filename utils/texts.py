# Barcha start funktsiyasi
START = \
"""
Assalomu alaykum, {}! 👋
"""

# Yangi anime

ANIME_NAME = \
"""
Anime nomini kiriting: 🎬
""" 

ANIME_UZNAME = \
"""
Uzbekcha nomini kiriting: 📛
""" 

SHIKIMORE_URL = \
"""
Shikimore URL manzilini kiriting: 🔗
"""

SELECT_REJISSYOR = \
"""
Rejissyorni tanlang: 🎥
"""

def addAnime(**kwargs):
    newanime = ''
    
    newanime += 'Tasdiqlash ✅\n\n'
    newanime += f"Nomi: {kwargs['name']}\n"
    newanime += f"Uzbekcha Nomi: {kwargs['uz_name']}\n"
    newanime += f"Shikimore URL: {kwargs['shikimore_url']}\n"
    newanime += f"Rejissyor ismi: {kwargs['first_name']}\n"
    
    return newanime


def rejissyor_nontification(**kwargs):
    newanime = ''
    
    newanime += 'Yangi Anime 🎉\n\n'
    newanime += f"Nomi: {kwargs['name']}\n"
    newanime += f"Uzbekcha Nomi: {kwargs['uz_name']}\n"
    newanime += f"Shikimore URL: {kwargs['shikimore_url']}\n"
    

    return newanime



SUCESS_ADMIN = \
"""
Anime rejissorga muvaffaqiyatli yuborildi! 🎉
"""

REJISSYOR_ACCEPT = \
"""
✅ Muvaffaqiyatli qabul qilindi! Yaxshi ish! 💪
"""


REJISSOR_SOURCE_FILE = \
"""
Kerakli source fayllarni kiriting! 📂
"""


SELECT_TRANSLATORS  = \
"""
Kerakli tarjimonlarni tanlang va "Yuborish" tugmasini bosing! ✍️
(bir nechta tarjimonni tanlash mumkin)
"""



SUCCESS_TRANSLATORS = \
"""
Siz tanlagan tarjimonlarga fayllar muvaffaqiyatli yuborildi! 📩
"""


NOT_TRANSLATORS = \
"""
Siz hali tarjimon tanlamadingiz. Iltimos, tanlang! 🧐
"""

WORKER_NOTIFICATION_TEXT = \
"""
Sizga yangi topshiriq berildi! 🎯
"""


TRANSLATOR_ACCEPT = \
"""
Siz faylni qabul qildingiz. Rahmat! Ishni tugatib, "Bajarildi" tugmasini bosing. ✔️
"""



TRANSLATORS_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang. 📤
""" 



TRANSLATORS_FEEDBACK = \
"""
Yaxshi fayl qabul qilindi! Ish bo'yicha izoh qoldiring. 📝
"""




TRANSLATOR_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. ✨
Rejissyor tomonidan fayl tekshirilib, sizga habar beriladi! 📢
"""



CANCELLED = \
"""
Tarjima bekor qilindi. ❌
"""


CANCELLED_TRANSLATOR_SEND = \
"""
Tarjima rejissyor tomonidan rad etildi. Iltimos, tekshirib qayta yuboring. 🔄
"""


VOICE_SOURCE_FILE = \
"""
Ovoz aktyorlari uchun source faylni kiriting! 🎤
"""


SUCCES_TRANSLATOR_FILE = \
"""
Siz tashlagan tarjimani rejissyor qabul qildi! ✅
"""

VOICE_WORKER_LIST = \
"""
Ovoz aktyorlarini tanlang! 🎭
"""



SUCCESS_VOICE_AKTYOR = \
"""
Siz tanlagan ovoz aktyorlariga fayllar yuborildi! 🎙️
"""


NOT_VOICE_AKTYOR = \
"""
Siz hali ovoz aktyorlarini tanlamadingiz. Iltimos, tanlang! 🧐
"""


VOICE_AKTYOR_ACCEPT = \
"""
Siz faylni qabul qildingiz. Rahmat! Ishni tugatib, "Bajarildi" tugmasini bosing. ✔️
"""



VOICE_AKTYOR_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang. 📤
""" 



VOICE_AKTYOR_FEEDBACK = \
"""
Yaxshi fayl qabul qilindi! Ish bo'yicha izoh qoldiring. 📝
"""




VOICE_AKTYOR_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. ✨
Rejissyor tomonidan fayl tekshirilib, sizga habar beriladi! 📢
"""



CANCELLED_VOICE_AKTYOR_SEND = \
"""
Siz tashlagan fayl rejissyor tomonidan rad etildi. Iltimos, tekshirib qayta yuboring. 🔄
"""


SUCCES_VOICE_AKTYOR_FILE = \
"""
Siz tashlagan faylni rejissyor qabul qildi! ✅
"""



TIMER_SOURCE_FILE = \
"""
Timerlar uchun source faylni kiriting! ⏱️
"""



TIMER_WORKER_LIST = \
"""
Timerchilarni tanlang! ⏲️
"""


NOT_TIMER = \
"""
Siz hali timerlarni tanlamadingiz. Iltimos, tanlang! 🧐
"""

SUCCES_TIMER = \
"""
Siz yuborgan fayl timerchilarga yuborildi! 📤
"""

TIMER_ACCEPT = \
"""
Siz faylni qabul qildingiz. Rahmat! Ishni tugatib, "Bajarildi" tugmasini bosing. ✔️
"""



TIMER_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang. 📤
""" 


TIMER_FEEDBACK = \
"""
Yaxshi fayl qabul qilindi! Ish bo'yicha izoh qoldiring. 📝
"""


TIMER_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. ✨
Rejissyor tomonidan fayl tekshirilib, sizga habar beriladi! 📢
"""



CANCELLED_TIMER_SEND = \
"""
Fayl rejissyor tomonidan rad etildi. Iltimos, tekshirib qayta yuboring. 🔄
"""


CANCELLED_TIMER_FILE = \
"""
Fayl bekor qilindi. ❌
"""



TIMER_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang. 📤
""" 


TIMER_FEEDBACK = \
"""
Yaxshi fayl qabul qilindi! Ish bo'yicha izoh qoldiring. 📝
"""



TIMER_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. ✨
Rejissyor tomonidan fayl tekshirilib, sizga habar beriladi! 📢
"""



SUCCESS_ANIME = \
"""
✅ Anime muvaffaqiyatli tugatildi! Yaxshi ish! 👏
"""


SUCCESS_ANIME_WORKER = """
✅ Rejissyor muvaffaqiyatli qabul qildi. 
"""



def translator_text(**kwargs):
    translator = ''
    
    translator += f"Tarjimon ismi: {kwargs['firstname']}\n"
    translator += f"Tarjimon tahallusi: {kwargs['stage_name']}\n"
    translator += f"Ish bo'yicha izoh: {kwargs['feedback']}\n"
    
    
    return translator
    
    

def voice_aktyor_text(**kwargs):
    voice_aktyor = ''
    
    voice_aktyor += f"Ovoz aktyor ismi: {kwargs['firstname']}\n"
    voice_aktyor += f"Ovoz aktyor tahallusi: {kwargs['stage_name']}\n"
    voice_aktyor += f"Ish bo'yicha izoh: {kwargs['feedback']}\n"
    
    return voice_aktyor
    
    

def timer_text(**kwargs):
    timer = ''
    
    timer += f"Timer ismi: {kwargs['firstname']}\n"
    timer += f"Timer tahallusi: {kwargs['stage_name']}\n"
    timer += f"Ish bo'yicha izoh: {kwargs['feedback']}\n"
    
    return timer
    
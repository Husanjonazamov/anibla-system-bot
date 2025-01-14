# all start funk
START = \
"""
Assalomu alaykum {}
"""

# all new anime

ANIME_NAME = \
"""
Anime nomini kiriting
""" 

ANIME_UZNAME = \
"""
Uzbekcha nomini kiriting
""" 

SHIKIMORE_URL = \
"""
Shikimore urlni kiriting!
"""


SELECT_REJISSYOR = \
"""
Rejissyorni tanlang!
"""


def addAnime(**kwargs):
    newanime = ''
    
    newanime += 'Tasdiqlash\n\n'
    newanime += f"Nomi: {kwargs['name']}\n"
    newanime += f"Uzbekcha Nomi: {kwargs['uz_name']}\n"
    newanime += f"Shikimore url: {kwargs['shikimore_url']}\n"
    newanime += f"Rejissyor ismi: {kwargs['first_name']}\n"
    
    return newanime


def rejissyor_nontification(**kwargs):
    newanime = ''
    
    newanime += 'Yangi Anime\n\n'
    newanime += f"Nomi: {kwargs['name']}\n"
    newanime += f"Uzbekcha Nomi: {kwargs['uz_name']}\n"
    newanime += f"Shikimore url: {kwargs['shikimore_url']}\n"
    

    return newanime



SUCESS_ADMIN = \
"""
Anime Rejissorga yuborildi!
"""

REJISSYOR_ACCEPT = \
"""
✅ Muvaffaqiyatli qabul qilindi!
"""


REJISSOR_SOURCE_FILE = \
"""
Kerakli source faylarni kiriting!
"""


SELECT_TRANSLATORS  = \
"""
Kerakli tarjimonlarni tanlang va Yuborih tugmasini boshing!
(bir nechta tarjimon tanlasangiz ham bo'ladi)
"""



SUCCESS_TRANSLATORS = \
"""
Siz tanlagan tarjimonlarga fayllar yuborildi
"""


NOT_TRANSLATORS = \
"""
Siz hali tarjimon tanlamadizgiz
"""

WORKER_NOTIFICATION_TEXT = \
"""
Sizga yangi topshiriq berildi!
"""


TRANSLATOR_ACCEPT = \
"""
Siz faylni qabul qildingiz. Rahmat! ishni tugatib bajarildi tugmasini bosing
"""



TRANSLATORS_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang
""" 



TRANSLATORS_FEEDBACK = \
"""
Yahshi fayl qabul qilindi ish boyicha izoh qoldiring
"""




TRANSLATOR_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. 
Rejissyor tomonidan fayl tekshirilib bo'lib habar beriladi!
"""



CANCELLED = \
"""
Tarjima bekor qilindi
"""


CANCELLED_TRANSLATOR_SEND = \
"""
Tarjima rejissyor tomonidan rad etildi iltimos tekshirib qayta yuboring
"""


VOICE_SOURCE_FILE = \
"""
Ovoz aktyorlari uchun source fayl kiriting
"""


SUCCES_TRANSLATOR_FILE = \
"""
Siz tashlagan tarjimani rejissyor qabul qildi!
"""

VOICE_WORKER_LIST = \
"""
Ovoz aktyorlarini tanlang!
"""



SUCCESS_VOICE_AKTYOR = \
"""
Siz tanlagan ovoz aktyorlariga fayllar yuborildi
"""


NOT_VOICE_AKTYOR = \
"""
Siz hali ovoz aktyorlarini tanlamadizgiz
"""


VOICE_AKTYOR_ACCEPT = \
"""
Siz faylni qabul qildingiz. Rahmat! ishni tugatib bajarildi tugmasini bosing
"""



VOICE_AKTYOR_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang
""" 



VOICE_AKTYOR_FEEDBACK = \
"""
Yahshi fayl qabul qilindi ish boyicha izoh qoldiring
"""




VOICE_AKTYOR_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. 
Rejissyor tomonidan fayl tekshirilib bo'lib habar beriladi!
"""



CANCELLED_VOICE_AKTYOR_SEND = \
"""
Siz tashlagan fayl rejissyor tomonidan rad etildi iltimos tekshirib qayta yuboring
"""


SUCCES_VOICE_AKTYOR_FILE = \
"""
Siz tashlagan faylni rejissyor qabul qildi!
"""



TIMER_SOURCE_FILE = \
"""
Timerlar uchun source file kiriting!
"""



TIMER_WORKER_LIST = \
"""
Timerchilarni tanlang!
"""


NOT_TIMER = \
"""
Siz hali timerlarni tanlamadingiz tanlamadizgiz
"""

SUCCES_TIMER = \
"""
Siz yuborgan fayl timerchilarga yuborildi
"""

TIMER_ACCEPT = \
"""
Siz faylni qabul qildingiz. Rahmat! ishni tugatib bajarildi tugmasini bosing
"""



TIMER_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang
""" 


TIMER_FEEDBACK = \
"""
Yahshi fayl qabul qilindi ish boyicha izoh qoldiring
"""


TIMER_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. 
Rejissyor tomonidan fayl tekshirilib bo'lib habar beriladi!
"""



CANCELLED_TIMER_SEND = \
"""
Fayl rejissyor tomonidan rad etildi iltimos tekshirib qayta yuboring
"""


CANCELLED_TIMER_FILE = \
"""
Fayl bekor qilindi
"""



TIMER_FILE_SEND = \
"""
Bajarilgan ishni qayta yuklang
""" 


TIMER_FEEDBACK = \
"""
Yahshi fayl qabul qilindi ish boyicha izoh qoldiring
"""



TIMER_WORK_SEND = \
"""
Sizning faylingiz muvaffaqiyatli tarzda rejissorga yuborildi. 
Rejissyor tomonidan fayl tekshirilib bo'lib habar beriladi!
"""



SUCCESS_ANIME = \
"""
✅ Anime muvaffaqiyatli tugatildi!
"""

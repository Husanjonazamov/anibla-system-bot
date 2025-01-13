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

TRANSLATOR_NOTIFICATION_TEXT = \
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
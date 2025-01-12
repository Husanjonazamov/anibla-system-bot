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
from aiogram.dispatcher.filters.state import State, StatesGroup


class NewAnimeState(StatesGroup):
    name = State()
    uz_name = State()
    shikimore_url = State()
    rejissor = State()
    check = State()
    
    
class RejissyorState(StatesGroup):
    rejissyor_id = State()
    file = State()
    worker = State()
    worker_send = State()
    
    
    
class Translators(StatesGroup):
    rejissyor_id = State()
    file = State()
    feedback = State()
    
    
class TranslatorCencelledState(StatesGroup):
    rejissyor_id = State()
    file = State()
    feedback = State()
    
    
class RejisyorVoiceAktyorState(StatesGroup):
    rejissyor_id = State()
    file = State()
    voice_worker = State()
    
    
class VoiceAktyorState(StatesGroup):
    rejissyor_id = State()
    file = State()
    feedback = State()
    
    
    
class VoiceAktyorCenceledState(StatesGroup):
    rejissyor_id = State()
    file = State()
    feedback = State()




class RejissyorTimerState(StatesGroup):
    rejissyor_id = State()
    file = State()
    timer_worker = State()
    
    
class TimerState(StatesGroup):
    rejissyor_id = State()
    file = State()
    feedback = State()
    
    
class TimerCenceledState(StatesGroup):
    rejissyor_id = State()
    file = State()
    feedback = State()

    
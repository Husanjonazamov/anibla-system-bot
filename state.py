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
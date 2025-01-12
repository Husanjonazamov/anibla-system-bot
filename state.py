from aiogram.dispatcher.filters.state import State, StatesGroup


class NewAnimeState(StatesGroup):
    name = State()
    uz_name = State()
    shikimore_url = State()
    rejissor = State()
    check = State()
    
    
class RejissyorState(StatesGroup):
    file = State()
    worker = State()
    worker_send = State()
    
    
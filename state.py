from aiogram.dispatcher.filters.state import State, StatesGroup


class NewAnime(StatesGroup):
    name = State()
    uz_name = State()
    shikimore_url = State()
    rejissor = State()
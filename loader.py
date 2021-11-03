from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils import Config

conf = Config('config.json')
bot = Bot(token=conf.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

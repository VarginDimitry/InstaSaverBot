import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from selenium import webdriver
from utils import Config

conf = Config('config.json')

options = webdriver.ChromeOptions()
if logging.root.level <= logging.INFO:
    options.add_argument("headless")
browser = webdriver.Chrome(executable_path="./chromedriver", options=options)


bot = Bot(token=conf.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

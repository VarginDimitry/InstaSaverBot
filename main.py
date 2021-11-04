import logging

from aiogram import Bot, Dispatcher, executor

from utils import Config
from loader import dp
import handlers


async def on_startup(dispatcher):
    logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,
                           skip_updates=True)

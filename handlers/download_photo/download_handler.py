import asyncio
import os
import random
import string
from http.client import HTTPMessage
import logging
import re
import urllib
from urllib.request import urlretrieve
import uuid
from typing import List

import aiohttp
from aiogram import types
from aiogram.types import InputMedia
from aiogram.utils.exceptions import BadRequest
from bs4 import BeautifulSoup, Tag

from loader import dp, browser, bot
from utils import Logger


@dp.message_handler(regexp=r"^https://www.instagram.com/p/")
async def download_handler(message: types.Message):
    Logger.log_photo_mes(message)
    await message.answer("I has started downloading your photo...")

    browser.get(message.text)
    await asyncio.sleep(2)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    if 'This Account is Private' in soup.text:
        await message.answer('This account is private. I can not download it :(')
    else:
        first_comment = soup.find('div', {'class': 'C4VMK'})
        post_owner = soup.find('div', {'class': 'PQo_0 RqtMr'})
        if first_comment and post_owner:
            logging.log(logging.DEBUG, f"{first_comment=}")
            logging.log(logging.DEBUG, f"{post_owner=}")

            post_message = first_comment.find('span').text if \
                first_comment.find('span') and first_comment.find('a') and post_owner.find('a') \
                and post_owner.find('a').text == first_comment.find('a').text else ""
            logging.log(logging.DEBUG, f"{post_message=}")
        else:
            post_message = ""
            logging.log(logging.DEBUG, f"Post hasn't, text")

        answer_text = f"{post_message.strip()}\n\nDownloaded with @cartman_saver_bot"
        images = [
            x.get('src') for x in soup.find_all(
                'img', {"class": "FFVAD", "alt": re.compile("^Photo.*by ")})
        ]
        logging.log(logging.DEBUG, f"{images=}")
        size = len(images)
        if size > 10:
            await message.answer(f"There are too many images in this case!")
        elif size < 1:
            await message.answer(f"There are not images")
        else:
            for image in images:
                try:
                    await message.answer_photo(image, caption=answer_text)
                except BadRequest as ex:
                    if ex.__str__() == 'Media_caption_too_long':
                        await message.answer('Media you send is too long. I can not download it :(')


@dp.message_handler(regexp=r"^http[s]?://")
async def download_error_handler(message: types.Message):
    await message.answer(
        "The link you send is incorrect. If you believe you send a right link then write me @dmitryvargin")


@dp.message_handler()
async def echo(message: types.Message):
    random_chars = ''.join(random.choices(f"{string.digits}{string.ascii_letters}", k=11))
    url_example = f"https://www.instagram.com/p/{random_chars}/"
    await message.answer(f"Send me some instagram photo link.\n For example:\n{url_example}")

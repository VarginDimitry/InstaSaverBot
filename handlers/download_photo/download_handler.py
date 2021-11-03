import asyncio
import os
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
from bs4 import BeautifulSoup, Tag

from loader import dp, browser, bot


@dp.message_handler(regexp=r"^https://www.instagram.com/p/")
async def download_handler(message: types.Message):
    await message.answer("I has started downloading your photo...")
    try:
        browser.get(message.text)
        await asyncio.sleep(1.5)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        first_comment = soup.find('div', {'class': 'C4VMK'})
        post_owner = soup.find('div', {'class': 'PQo_0 RqtMr'}).find('a').text
        post_message = first_comment.find('span').text if post_owner == first_comment.find('a').text else ""
        answer_text = f"{post_message.strip()}\n\nDownloaded with @cartman_saver_bot"
        images = [
            x.get('src') for x in soup.find_all(
            'img', {"class": "FFVAD", "alt": re.compile("^Photo by ")})
        ]
        # InputMedia()
        size = len(images)
        if size == 1:
            await message.answer_photo(images[0])
            await message.answer(answer_text)
        elif size > 1:
            await message.answer_media_group(media=images)
            await message.answer(answer_text)
        elif size > 10:
            await message.answer(f"There are too many images in this case!")
        else:
            await message.answer(f"There are not images")
    except Exception as ex:
        raise ex


@dp.message_handler(regexp=r"^http[s]?://")
async def download_error_handler(message: types.Message):
    await message.answer(
        "The link you send is incorrect. If you believe you send a right link then write me @dmitryvargin")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

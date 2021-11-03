import asyncio
import logging

import aiohttp
from aiogram import types
from aiohttp import ClientResponse

from loader import dp


@dp.message_handler(regexp=r"^http[s]?://")
async def download_handler(message: types.Message):
    await message.answer("I has started downloading your photo...")
    async with aiohttp.ClientSession() as session:
        async with session.get(message.text) as res:
            res_status = res.status
            res_text = (await res.text())[:100]
            await message.answer(f"{res_status=}\n{res_text=}")
    await message.answer(f"Your link:\n{message.text}")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

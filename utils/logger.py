import logging

from aiogram import types


class Logger:

    @staticmethod
    def info(*args, **kwargs):
        logging.info(*args, **kwargs)

    @staticmethod
    def error(*args, **kwargs):
        logging.error(*args, **kwargs)

    @staticmethod
    def log_photo_mes(mes: types.Message):
        name = f"{mes.from_user.full_name} ({mes.from_user.id})" if mes.from_user.full_name \
            else f"{mes.from_user.username} ({mes.from_user.id})" if mes.from_user.username \
            else f"{mes.from_user.id}"
        logging.info(f"User {name} requires a photo {mes.text}")

    @staticmethod
    def log_mes(mes: types.Message):
        name = f"{mes.from_user.full_name} ({mes.from_user.id})" if mes.from_user.full_name \
            else f"{mes.from_user.username} ({mes.from_user.id})" if mes.from_user.username \
            else f"{mes.from_user.id}"
        logging.info(f"User {name} send {mes.text}")

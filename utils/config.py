import json
import os


class Config:

    __token: str = None
    __admins: tuple = None

    @property
    def API_TOKEN(self):
        return Config.__token

    @property
    def ADMIN_IDS(self):
        return Config.__admins

    def __init__(self, file_name=None):
        self.__base_url = os.getcwd()
        if file_name:
            self.read_config(file_name)

    def read_config(self, file_name):
        with open(os.path.join(self.__base_url, file_name)) as f:
            conf = json.loads(f.read())
            Config.__token = conf.get('API_TOKEN')
            Config.__admins = tuple(conf.get('admins'))
            if Config.__token is None or Config.__admins is None:
                raise IOError(f"Config dont include TOKEN or ADMIN_IDS")
        return self

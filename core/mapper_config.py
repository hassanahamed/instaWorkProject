
from .appConstants import *

class MemberConfig():
    config = {}

    def __init__(self,config=DEFAULT_MEMBER_CONFIG):
        self.config = config

    def get_data(self, data):
        mapped_data = {}
        for item in self.config.keys():
            value = data.get(self.config[item])
            mapped_data[item] = value.strip() if isinstance(value, str) else value
        return mapped_data

        
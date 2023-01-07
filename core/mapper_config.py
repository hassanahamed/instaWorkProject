
from .appConstants import *

class MemberConfig():
    config = {}

    def __init__(self,config=DEFAULT_MEMBER_CONFIG):
        self.config = config

    def get_data(self, data):
        mapped_data = {}
        for item in self.config.keys():
            mapped_data[item] = data.get(self.config[item])
        return mapped_data

        
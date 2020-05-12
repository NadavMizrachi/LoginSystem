import Database
import Exceptions
import Validator

"""
    This class represents user who registered to the database.
    user on the system can make those operations:
        1. Pull his private data that was saved on the database.
        2. Push data to save on the database (the data will append to the current data - the
            last data can't be deleted). 
            In order to save data, the user has to save the data on LOCALDATA (by 
            the method set_local_data), and then use push_data method.
"""

class User:

    def __init__(self, username, passwd, validator):
        self.username = username
        self.passwd = passwd
        self.validator = validator
        self.local_data = ""

    def pull_data(self):
        self.pulled_data = self.validator.retrieve_data(self)

    def push_data(self):
        if self.__is_not_empty(self.local_data):
            self.validator.update_data(self, self.local_data)
            self.local_data = ""

    def __is_not_empty(self, data):
        return len(data) != 0

    def get_local_data(self):
        return self.local_data

    def get_pulled_data(self):
        return self.pulled_data

    def set_local_data(self, data):
        self.local_data += data

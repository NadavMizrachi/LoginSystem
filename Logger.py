import datetime
import os

"""
    This class take care about logging the system events on txt file.
    The admin will be able to extract those logs.
    The logs will be saved on file that will be created.
"""

class Logger:
    log_file_name = 'log.txt'

    def __init__(self):
        self.log_file = Logger.log_file_name
        self.__init_files()

    def __init_files(self):
        if self.__is_file_not_exists(Logger.log_file_name):
            open(Logger.log_file_name, 'w+')

    def __is_file_not_exists(self, log_file_name):
        return os.path.exists(log_file_name) == False

    def user_created_log(self, key):
        with open(self.log_file, 'a+') as lg_f:
            data = self.__create_creation_string(key)
            lg_f.write(data)

    def user_pulled_data_log(self, key):
        with open(self.log_file, 'a+') as lg_f:
            data = self.__pulling_data_string(key)
            lg_f.write(data)

    def __pulling_data_string(self, key):
        return self.__create_timestamp() + " " +str(key) + " pulled data.\n"

    def __create_creation_string(self, key):
        return self.__create_timestamp() + " " + str(key) + " was created.\n"

    def __create_timestamp(self):
        return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def user_pushed_data_log(self, key):
        with open(self.log_file, 'a+') as lg_f:
            data = self.__create_user_pushed_data_log_string(key)
            lg_f.write(data)

    def __create_user_pushed_data_log_string(self, key):
        return self.__create_timestamp() + " " + str(key) + " saved data.\n"

    def logging_log(self, key):
        with open(self.log_file, 'a+') as lg_f:
            data = self.__create_logging_log_string(key)
            lg_f.write(data)

    def __create_logging_log_string(self, key):
        return self.__create_timestamp() + " " + str(key) + " logged to system.\n"

    def get_logs(self):
        with open(self.log_file_name, 'r') as log_file:
            return log_file.readlines()
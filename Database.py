import os
import Exceptions
import IDB
import datetime
import Logger
import Admin

""" Database that will save the users credentials records on txt file. 
    The format of the records in this file is:
    
    USERNAME1    PASSWORD1
    USERNAME2    PASSWORD2
    ...         ...
    ...         ...
    
    And so on.
    
    For each user, the database will save his data on file. The file name will be associated 
    with the user by his name (The database will create those files).
    Example:
        If the username is: NADAV
        then the data will be saved on NADAV.dat file.
    the data files will be saved on special directory.
   
"""


class Database(IDB.IDB):
    file_name = 'DB.txt'
    data_files_dir_name = 'data_files'

    def __init__(self):
        self.log_system = Logger.Logger()
        self.__init_db_files()

    def __init_db_files(self):
        if self.__is_file_not_exists(Database.file_name):
            open(Database.file_name, 'w+')
        if self.__is_directory_not_exits(Database.data_files_dir_name):
            os.mkdir(Database.data_files_dir_name)

    def __is_file_not_exists(self, file_name):
        return os.path.exists(Database.file_name) == False

    def __is_directory_not_exits(self, dir_name):
        return os.path.isdir(dir_name) == False

    def validate_user(self, username, passwd):
        with open(Database.file_name, 'r') as db_file:
            records = db_file.read().splitlines()
            for record in records:
                if self.__username_match(record, username):
                    if self.__password_match(record, passwd):
                        self.log_system.logging_log(username)
                        return  # User is valid
                    else:
                        raise Exceptions.WrongPassword(username)
        raise Exceptions.UserDoesNotExist

    def __username_match(self, record, username):
        if len(record.split()) != 2:
            return False
        return record.split()[0] == username

    def __password_match(self, record, passwd):
        if len(record.split()) != 2:
            return False
        return record.split()[1] == passwd

    def create_user(self, username, passwd):
        if self.__is_user_exist(username):
            raise Exceptions.UserNameAlreadyExists(username)
        if self.__unvalid_username(username):
            raise Exceptions.UnvalidUsername()
        if self.__unvalid_password(passwd):
            raise Exceptions.UnvalidPassword()
        self.__create_user_record(username, passwd)
        self.__create_user_datafile(username)
        self.log_system.creation_log(username)

    def __is_user_exist(self, username):
        with open(Database.file_name, 'r') as db_file:
            records = db_file.read().splitlines()
            for record in records:
                if self.__username_match(record, username):
                    return True
        return False

    def __unvalid_username(self, username):
        return len(username) <= 1

    def __unvalid_password(self, passwd):
        return len(passwd) <= 1

    def __create_user_record(self, username, passwd):
        with open(Database.file_name, 'a+') as db_file:
            record = "\n" + username + " " + passwd
            db_file.write(record)

    def __create_user_datafile(self, username):
        if self.__is_directory_not_exits(Database.data_files_dir_name):
            os.mkdir(Database.data_files_dir_name)
        data_file_name = self.__generate_user_datafile_name(username)
        new_data_file = open(data_file_name, 'w')
        new_data_file.close()

    def __generate_user_datafile_name(self, username):
        name = os.path.join(Database.data_files_dir_name, username + ".dat")
        return name

    def get_user_data(self, username):
        with open(self.__generate_user_datafile_name(username), 'r') as data_file:
            data = data_file.read()
            self.log_system.pulling_data_log(username)
            return data

    def update_data(self, username, new_data):
        with open(self.__generate_user_datafile_name(username), 'a+') as data_file:
            self.__write_data_timestamp(data_file)
            data_file.write(new_data)
            self.__write_seperator(data_file)
            self.log_system.saving_data_log(username)

    def __write_data_timestamp(self, data_file):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_file.write(str(timestamp) + '\n')

    def __write_seperator(self, data_file):
        separator = "\n****\n"
        data_file.write(separator)

    def admin_login(self, username, password):
        try:
            self.__check_username_and_password(username, password)
        except Exceptions.WrongCredentails:
            raise Exceptions.WrongCredentails

    def __check_username_and_password(self, username, password):
        if username != Admin.Admin.username or password != Admin.Admin.password:
            raise Exceptions.WrongCredentails

    def get_logs(self):
        return self.log_system.get_logs()

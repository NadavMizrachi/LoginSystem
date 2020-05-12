import Validator
import Database
import User
from LoginUtil import *
import Exceptions
import os

"""
    This is a CMD interface application for the user of the system.
"""

class App():
    def __init__(self):
        self.validator = Validator.Validator(Database.Database())

    def start(self):
        self.__clear_console()
        self.ask_loging_signup_quit()

    def ask_loging_signup_quit(self):
        prompt_str = "For logging to system press [l]\n"\
                        "For signing up press [s]\n"\
                        "To quit press [q]\n"
        self.choice = input(prompt_str)
        self.exec_choice()

    def exec_choice(self):
        self.__clear_console()
        if self.choice == "l":
            self.login()
        elif self.choice == "s":
            self.signup()
        elif self.choice == "q":
            self.quit_app()
        else:
            print("Unknown operation...")
            self.ask_loging_signup_quit()

    def login(self):
        username , password = LoginUtil.get_login_usr_pss_from_user()
        try:
            self.user = self.validator.login(username, password)
            self.__clear_console()
            print("Wellcome " + str(self.user.username) + "! Logging succeed.")
            self.start_user_work()
        except Exceptions.UserDoesNotExist:
            self.__clear_console()
            print("Username does not exist")
            self.ask_loging_signup_quit()
        except Exceptions.WrongPassword:
            self.__clear_console()
            print("Wrong password")
            self.ask_loging_signup_quit()

    def start_user_work(self):
        prompt =    "For pulling data type [pull]\n" \
                    "For push data in DB type [push]\n" \
                    "For adding local data type [localdata]\n" \
                    "For quit press [q]\n"
        self.user_operation = input(prompt)
        self.process_user_operation()

    def process_user_operation(self):
        self.__clear_console()
        if self.user_operation == "pull":
            self.pull_user_data_from_db()
        elif self.user_operation == "push":
            self.push_user_data_to_db()
        elif self.user_operation == "localdata":
            self.set_user_localdata()
        elif self.user_operation == "q":
            self.ask_for_pushing()
            self.quit_app()
        else:
            print("Unknown operation.")
        self.start_user_work()

    def pull_user_data_from_db(self):
        self.user.pull_data()
        print(self.user.get_pulled_data())

    def push_user_data_to_db(self):
        self.user.push_data()
        print("data pushed successfully.")

    def set_user_localdata(self):
        localdata = input("Enter local data : ")
        self.user.set_local_data(localdata)
        print("Local data has been set.")

    def ask_for_pushing(self):
        self.choice = input("Push local data on DB? press y or n :")
        if self.choice == "y":
            self.user.push_data()

    def signup(self):
        print("Siging up to system:")
        username, passwd = self.__get_username_password()
        try:
            self.user = self.validator.create_user(username, passwd)
        except Exceptions.UserNameAlreadyExists:
            self.__clear_console()
            print("Username already exists!")
            self.ask_loging_signup_quit()
        except Exceptions.UnvalidPassword:
            self.__clear_console()
            print("Invalid Password.")
            self.ask_loging_signup_quit()
        except Exceptions.UnvalidUsername:
            self.__clear_console()
            print("Invalid Username.")
            self.ask_loging_signup_quit()
        else:
            self.__clear_console()
            print("Wellcome " + str(self.user.username) + "! Successful signing up!")
            self.start_user_work()

    def __get_username_password(self):
        username = input("Username : ")
        passwd = getpass.getpass("Password : ")
        passwd_con = getpass.getpass("Type again Password : ")
        if passwd != passwd_con:
            print("Error, password are not same.")
            self.ask_loging_signup_quit()
        return username , passwd

    def __clear_console(self):
        os.system('cls')

    def quit_app(self):
        self.__clear_console()
        print("Quiting the app!")
        exit(0)
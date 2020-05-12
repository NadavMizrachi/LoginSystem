from LoginUtil import *
import os
import Database
import Exceptions

"""
    This is a CMD interface application for the admin of the system.
"""
class AdminApp():

    def __init__(self):
        self.db = Database.Database()

    def start(self):
        self.__clear_console()
        self.ask_for_credentials()

    def ask_for_credentials(self):
        username, password = LoginUtil.get_login_usr_pss_from_user()
        try:
            self.db.admin_login(username, password)
            self.__print_wellcome_admin()
            self.start_work()
        except Exceptions.WrongCredentails:
            print("Wrong Credentails! quiting.")
            exit()

    def __print_wellcome_admin(self):
        self.__clear_console()
        print("Wellcome my lord!")

    def start_work(self):
        self.choice = input("Please choose operation:\n"\
                            "For extract logs press [l].\n"\
                            "For quiting press [q].\n")
        self.exec_choice()

    def exec_choice(self):
        if self.choice == "l":
            self.show_logs()
        elif self.choice == "q":
            self.quit_app()
        else:
            print("Unknown operation!")
            self.start_work()

    def show_logs(self):
        logs_data = self.db.get_logs()
        self.__print_logs(logs_data)
        self.start_work()

    def __print_logs(self, logs_data):
        self.__clear_console()
        for line in logs_data:
            print(line)
        print("\n\n\n")

    def quit_app(self):
        print("Bye!")
        exit()

    def __clear_console(self):
        os.system('cls')
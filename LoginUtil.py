import getpass
class LoginUtil:
    @staticmethod
    def get_login_usr_pss_from_user():
        print("Logging to system:")
        username = input("Username : ")
        password = getpass.getpass()
        return username , password
from IDB import *
import User
import Exceptions

"""
    This class is a proxy between the User to his database. This class expect to get
    Database which implements the abstract class IDB (Without knowing how the DB is implemented - ether with File,
    or SQLdb and so on). 
"""
class Validator:

    def __init__(self, DB):
        self.db = DB

    def login(self, username, passwd):
        try:
            self.db.validate_user(username, passwd)
            return User.User(username, passwd, self)
        except Exceptions.UserDoesNotExist:
            raise Exceptions.UserDoesNotExist
        except Exceptions.WrongPassword:
            raise Exceptions.WrongPassword

    def create_user(self,username, passwd):
        try:
            self.db.create_user(username, passwd)
            return User.User(username, passwd, self)
        except Exceptions.UserNameAlreadyExists:
            raise Exceptions.UserNameAlreadyExists
        except Exceptions.UnvalidPassword:
            raise Exceptions.UnvalidPassword

    def update_data(self, user, data):
        self.db.update_data(user.username, data)

    def retrieve_data(self, user):
        return self.db.get_user_data(user.username)

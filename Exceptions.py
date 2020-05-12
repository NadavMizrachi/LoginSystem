class UserNameAlreadyExists(Exception):
    pass

class WrongCredentails(Exception):
    pass

class WrongPassword(WrongCredentails):
    pass

class UserDoesNotExist(WrongCredentails):
    pass

class UnvalidPassword(Exception):
    pass

class UnvalidUsername(Exception):
    pass
# import Module_class.welcome_note as mc
from Module_class.welcome_note import wel as mc

def log_in():
    user = input('Enter your username: ')
    password = input('Enter your password: ')
    
    mc(user, password, 25)
log_in()
# File for function

#import necessary moduls
from pathlib import Path
from cryptography.fernet import Fernet


# for change on main(first) page
def main_page():
    print(
            "\n\tHello, it's your pasword manager.\n"
            "\tWhat would you do?\n"
            "\n\tAdd password:          'a'"
            "\n\tGet password:          'g'"
            "\n\tExit:                  'q'"
            )
    return(input('\n\tYour change: '))



# check key
def get_fernet():
    # read file with key
    with open('.key.txt', 'rb') as file:
        key = file.read()
    # check exist key
    if key != "b''":
        key = Fernet.generate_key()
        f = Fernet(key)
        with open('.key.txt', 'wb') as file:
            file.write(key)
    else:
        print(key)
        f = Fernet(key)
    # return fernet
    return(f)



# add password
def add_passwd(f):

    name = (input("\n\tName servise: ")).encode('utf-8')
    login = (input("\n\tLogin: ")).encode('utf-8')
    password = (input("\n\tPassword: ")).encode('utf-8')
    enc_password = f.encrypt(password)
    
    # Here will be sending data in data base

    password = f.decrypt(enc_password)

    print(
            "\n\tThis function in process"
            f"\n\tYour password: {password}"
            f"\n\tYour enc_password = {enc_password}"
          )



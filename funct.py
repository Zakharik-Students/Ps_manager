# File for function

#import necessary moduls
from pathlib import Path
from cryptography.fernet import Fernet
import psycopg2
from psycopg2 import Binary

# connection with data base
conn = psycopg2.connect(database = 'Ps_manager',
                        user = 'zakhar',
                        host = 'localhost',
                        port = 5432)
cur = conn.cursor()

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

    name = (input("\n\tName servise: "))
    login = (input("\n\tLogin: "))
    password = (input("\n\tPassword: "))
    enc_password = f.encrypt((password).encode("utf-8"))
    
    # Here will be sending data in data base
   
    cur.execute(
            "INSERT INTO Ps_manager (name, login, password) VALUES (%s, %s, %s)", (name, login, Binary(enc_password)),
            )

    conn.commit()
    cur.close()
    conn.close()
    
    print(
            "\n\tThis function in process"
            f"\n\tYour password: {password}"
            f"\n\tYour enc_password = {enc_password}"
          )



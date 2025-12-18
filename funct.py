# File for function

#import necessary moduls
from pathlib import Path
from cryptography.fernet import Fernet
from db_funct import connect_db, disconnect_db
from crypt_funct import get_fernet

# for change on main(first) page
def main_page():
    print(
            "\n\tHello, it's your pasword manager.\n"
            "\tWhat would you do?\n"
            "\n\tAdd password:          'a'"
            "\n\tGet password:          'g'"
            "\n\tChange password:       'c'"
            "\n\tDelete password:       'd'"
            "\n\tExit:                  'q'"
            "\n\tWatch anime girl       'w'"
            )
    return((input('\n\tYour change: ').lower()))



# check key
def get_fernet():
    key_path = Path('.key.txt')

    if not key_path.exists():
        key = Fernet.generate_key()
        key_path.write_bytes(key)
    else:
        key = key_path.read_bytes()
        if key == b'':
            key = Fernet.generate_key()
            key_path.write_bytes(key)

    return Fernet(key)

# add password
def add_passwd(f):

    name = (input("\n\tName servise: "))
    login = (input("\n\tLogin: "))
    password = (input("\n\tPassword: "))
    enc_password = f.encrypt((password).encode("utf-8"))

    conn, cur = connect_db() #def for connect to data base
    cur.execute(f"SELECT * FROM Ps_manager WHERE name = '{name}' AND login = '{login}';")
    rows = cur.fetchall()
    f = get_fernet()
    if rows:
        cur.execute(f"DELETE FROM Ps_manager WHERE name = '{name}' AND login = '{login}';")
        cur.execute(
            "INSERT INTO Ps_manager (name, login, password) VALUES (%s, %s, %s)", (name, login, enc_password),
            )
    else:
        cur.execute(
            "INSERT INTO Ps_manager (name, login, password) VALUES (%s, %s, %s)", (name, login, enc_password),
            )

    disconnect_db(conn, cur) 
    print("\n\t------------------------------------------------")
    print(f"\n\tThe additionl was successful")
    print("\n\t------------------------------------------------")

# def for get password by name
def get_by_name():
    name = input('\n\tYour name: ')
    conn, cur = connect_db() 
    cur.execute(f"SELECT * FROM Ps_manager WHERE name = '{name}';")
    rows = cur.fetchall()
    disconnect_db(conn, cur)
    f = get_fernet()
    print("\n\t--------------------------------------------------")
    if rows:
        for i in range(len(rows)):
            i = i-1
            name, login, pswd = rows[i]
            print(f"\n\t {name} | {login} | {f.decrypt(bytes(pswd)).decode('utf-8')}")
    else:
        print("\n\tYou have't passwort with this name...")
    print("\n\t--------------------------------------------------")            
    
    if not rows:
       print('\n\tDo you want try again?    y/n\n')
       choise = input('\tYour choise: ').lower()
       if choise == 'y':
           get_by_name()
           

# def for get password by login
def get_by_login():
    login = input('\n\tYour login: ')
    conn, cur = connect_db()
    cur.execute(f"SELECT * FROM Ps_manager WHERE login = '{login}';")
    rows = cur.fetchall()
    disconnect_db(conn, cur)
    f = get_fernet()
    print("\n\t--------------------------------------------------")
    if rows:
        for i in range(len(rows)):
            i = i-1
            name, login, pswd = rows[i]
            print(f"\n\t {name} | {login} | {f.decrypt(bytes(pswd)).decode('utf-8')}")
    else:
        print("\n\tYou have't passwort with this login... ")
    print("\n\t--------------------------------------------------")            

    if not rows:
       print('\n\tDo you want try again?    y/n\n')
       choise = input('\tYour choise: ').lower()
       if choise == 'y':
           get_by_login()


# funct for get password
def get_passwd():
    print("\n\tHow you want get your password?\n"
          "\n\tBy name:            'n'"
          "\n\tBy login:           'l'"
          )
    change = input("\n\tYour change: ").lower()
    if change == 'n':
        get_by_name()
    elif change == 'l':
        get_by_login()
    else:
        print('\n\tError input, try again.')
        get_passwd()


#def for change password
def ch_pswd(f):
    print('\n\tEnter data for change.')
    name = input('\n\tname: ')
    login = input('\n\tlogin: ')
    new_pswd = input('\n\tnew_password: ')
    enc_new_pswd = f.encrypt((new_pswd).encode('utf-8'))

    conn, cur = connect_db()
    cur.execute(f"DELETE FROM Ps_manager WHERE name = '{name}' AND login = '{login}';")
    cur.execute(
            "INSERT INTO Ps_manager (name, login, password) VALUES (%s, %s, %s)", (name, login, enc_new_pswd),
            )
    disconnect_db(conn, cur) 
    print('\n\t------------------------------------------')
    print('\n\tPassword was successesfully change')
    print('\n\t------------------------------------------')


def del_pswd():
    print('\n\tEnter data for delete.')
    name = input('\n\tname: ')
    login = input('\n\tlogin: ')

    conn, cur = connect_db()
    cur.execute(f"DELETE FROM Ps_manager WHERE name = '{name}' AND login = '{login}';")
    disconnect_db(conn, cur) 
    print('\n\t------------------------------------------')
    print('\n\tPassword was successesfully delete')
    print('\n\t------------------------------------------')



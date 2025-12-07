# The main file

# import
import sys
from cryptography.fernet import Fernet

# import modules
from funct import main_page, get_fernet, add_passwd, get_passwd

while True:
    change = main_page()
    if change.lower() == 'a':
        f = get_fernet()
        add_passwd(f)
    elif change.lower() == 'g':
        get_passwd()
    elif change.lower() == 'q':
        sys.exit(0)
    else:
        continue

import os
import hashlib

if os.name == 'nt':
    user = os.getlogin()
    passwd_path = rf"C:\Users\{user}\my_hashed_password.txt"
elif os.name == 'posix':
    passwd_path = r"%HOME/my_hashed_password.txt"

passwd = "Wdi2022"

salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', passwd.encode('utf-8'), salt, 1000000)

storage = salt + key

with open(passwd_path, "wb+") as f:
    f.write(storage)
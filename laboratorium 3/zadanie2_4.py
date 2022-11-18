import os
import hashlib

if os.name == 'nt':
    user = os.getlogin()
    passwd_path = rf"C:\Users\{user}\my_hashed_password.txt"
elif os.name == 'posix':
    passwd_path = r"%HOME/my_hashed_password.txt"

with open(passwd_path, "rb") as f:
    storage = f.read()
    get_salt = storage[:32]
    get_key = storage[32:]

usr_passwd = input("Podaj hasło: ")
usr_key = hashlib.pbkdf2_hmac('sha256', usr_passwd.encode('utf-8'), get_salt, 1000000)

if usr_key != get_key:
    print("Niepoprawne hasło, odmowa dostępu")
else:
    while True:
        name = input("Podaj ścieżkę pliku do edycji: ")
        print(name)

        print("[1] Zmiana nazwy \n"
              "[2] Kopiowanie   \n"
              "[3] Przeniesienie\n"
              "[4] Usunięcie    \n"
              "[5] Wyjście      \n")
        usr = int(input("Podaj operację: "))

        if usr == 1 or usr == 3:
            new_name = input("Podaj nową ścieżkę pliku: ")
            if os.path.isfile(new_name):
                print("Plik o takiej nazwie już istnieje!")
            else:
                os.rename(name, new_name)

        elif usr == 2:
            new_path = input("Podaj ścieżkę docelową kopiowania: ")
            if os.path.isfile(new_name):
                print("Plik o takiej nazwie już istnieje!")
            else:
                if os.name == 'nt':
                    os.system(f'copy {name} {new_path}')
                elif os.name == 'posix':
                    os.system(f'cp {name} {new_path}')

        elif usr == 4:
            try:
                os.remove(name)
            except OSError as err:
                print(f"Error: {err.filename} - {err.strerror}")

        elif usr == 5:
            break

        else:
            print("Podaj właściwą opcje")

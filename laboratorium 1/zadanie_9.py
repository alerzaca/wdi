saldo = 0
pin = 3579

while True:
    print("Dostępne opcje")
    print("[1] wpłata")
    print("[2] wypłata")
    print("[3] sprawdź saldo")
    print("[4] wyjdź")
    op = int(input("Podaj operację: "))

    if op == 4:
        exit("Zakończenie programu")
    elif op != 1 and op != 2 and op != 3:
        print("Podaj numer z zakresu 1-4 odpowiadający wybranej opcji")
    else:
        a = int(input("Podaj pin: "))
        if a == pin:
            if op == 1:
                wplata = int(input("Podaj kwote do wpłaty: "))
                saldo += wplata
                print("Wpłata przebiegła pomyślnie")
            elif op == 2:
                wyplata = int(input("Podaj kwote do wypłaty: "))
                if saldo >= wyplata:
                    saldo -= wyplata
                    print("Wypłata przebiegła pomyślnie")
                else:
                    print("Nie posiadasz takiej kwoty na koncie")
            elif op == 3:
                print("Twoje saldo wynosi:", saldo)
            print("Co chcesz zrobić w kolejnym kroku?")
        else:
            print("Pin niepoprawny, odmowa dostępu")
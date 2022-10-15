import random

odp = 'T'
while odp == 'T':
    print("Wprowadź dane")
    a = input()
    b = input()
    op = input()
    if op == '+':
        print(int(a) + int(b))
    elif op == '-':
        print(int(a) - int(b))
    elif op == '*':
        print(int(a) * int(b))
    elif op == '/':
        print(int(a) / int(b))
    elif op == '#':
        if a < b:
            print(random.randint(int(a), int(b)))
        else:
            print(random.randint(int(b), int(a)))
    elif op == '^':
        print(int(a) ** int(b))
    else:
        print("Wprowadzono niepoprawne dane")
    print("Czy chcesz wprowadzić nowe dane? (T/N)")
    odp = input()
    if odp == 'N':
        exit("Zakończenie programu")
    elif odp != 'T':
        exit("Błąd wprowadzania danych")

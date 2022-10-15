print("Podaj współczynniki")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a != 0:
    Delta = b**2-4*a*c
    print("Delta =", Delta)
    if Delta>0:
        print("x1 =", round((-b-(Delta**(1/2)))/2*a, 2))
        print("x2 =", round((-b+(Delta**(1/2)))/2*a, 2))
    elif Delta==0:
        print("x0 =", round(-b/2*a, 2))
    else:
        print("Funkcja nie ma miejsc zerowych w R, program nie obsługuje liczb zespolonych.")

else:
    print("Podana funkcja jest liniowa")
    if b!=0:
        print("x =", round(-c/b, 2))
    elif c==0:
        print("tożsamość - nieskończenie wiele rozwiązań")
    else:
        print("sprzeczność - brak rozwiązań")
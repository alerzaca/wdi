# Rozwiązywanie układu równań dla N niewiadomych metodą Cramera

import numpy as np

N = int(input("Podaj liczbę niewiadomych: "))
A = []
B = []

print("Podaj macierz współczynników równania:")
for i in range(N):
    a = [int(i) for i in input().split()]
    A.append(a)

print("Podaj kolumnę wyrazów wolnych:")
for i in range(N):
    b = [int(i) for i in input()]
    B.append(b)

print(A)
print(B)

# Rozwiązanie z wykorzystaniem biblioteki numpy

if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, B)
    print(x)
else:
    print("Układ jest sprzeczny lub nieoznaczony")

# Rozwiązanie bez użycia biblioteki (dużo bardziej skomplikowane)


# Rozwiązywanie układu równań dla N niewiadomych metodą Cramera

import numpy as np

# Rozwiązanie bez użycia biblioteki (dużo bardziej skomplikowane)

# def determinant(A, N):
#     temp = [0] * N
#     total = 1
#     det = 1
#
#     for i in range(0, N):
#         index = i
#         while index < N and A[index][i] == 0:
#             index += 1
#
#         if index == n:
#             continue
#         if index != i:
#             for j in range(0, N):
#                 A[index][j], A[i][j] = A[i][j], A[index][j]
#             det = det * int((-1) ** (index - i))
#
#         for j in range(0, N):
#             temp[j] = A[i][j]
#
#         for j in range(i + 1, N):
#             num1 = temp[i]
#             num2 = A[j][i]
#
#             for k in range(0, N):
#                 A[j][k] = (num1 * A[j][k]) - (num2 * temp[k])
#
#             total = total * num1
#
#     for i in range(0, A):
#         det = det * A[i][i]
#
#     return int(det / total)  # Det(kA)/k=Det(A);
#
# def inversion(A, N):
#
# def dot_product(A, B):
#     dot = 0
#     for i in range(len(A))
#         dot += (A[i] * B[i])

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

# if determinant(A, N) != 0:
#    A_inv = inversion(A, N)
#    x = dot_product(A_inv, B)
#    print(x)
# else:
#    print("Układ jest sprzeczny lub nieoznaczony")

# Rozwiązanie z wykorzystaniem biblioteki numpy

if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, B)
    print(x)
else:
    print("Układ jest sprzeczny lub nieoznaczony")

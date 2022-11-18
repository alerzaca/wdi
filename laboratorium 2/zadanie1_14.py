from collections import OrderedDict


def insert(str_s, in_s, pos_i):
    return str_s[:pos_i] + in_s + str_s[pos_i:]


letters = [chr(i) for i in range(97, 123)]
occurrence = OrderedDict.fromkeys(letters, 0)
user_input = input("Wprowadź  napis: ").lower()

for i in user_input:
    if i in occurrence:
        occurrence[i] += 1

unique = [i for i in occurrence if occurrence[i] == 1]

print(occurrence)
print(unique)

N = 1
N_2 = 1
for i in range(1, len(unique) + 1):
    N *= (len(user_input) + i)
    N_2 *= (len(user_input) + i) * len(letters)
print("Istnieje", N, "możliwych rozszerzonych napisów")
print("Istnieje", N_2, "możliwych rozszerzonych napisów (licząc wszystkie litery alfabetu)")

# Przykład: dla napisu długości 5 i dla 2 unikalnych znaków:
# 1 znak - 6 możliwości ustawienia
# 2 znak - 7 możliwości ustawienia
# itp. itd.





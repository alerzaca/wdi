num1 = int(input('Podaj pierwszą liczbę: '))
num2 = int(input('Podaj drugą liczbę: '))

"""
sprawdzanie czy podane liczby są/nie są ujemne
oraz wyciąganie wartości bezwzględnej
"""
if num1 < 0 and num2 < 0:
    exit("Obie liczby są mniejsze od zera, kniec programu")
elif num1 < 0:
    num1 = abs(num1)
elif num2 < 0:
    num2 = abs(num2)

# operacje sumy i różnicy
print(f'Suma podanych liczb to: {num1 + num2}')
print(f'Różnica podanych liczb to: {num1 - num2}')

"""
sprawdzanie czy iloczyn
jest równy 10, Yay!
"""
if num1 * num2 == 10:
    print(f'Iloczyn podanych liczb to: {num1 * num2} Yay!')
else:
    print(f'Iloczyn podanych liczb to: {num1 * num2}')

# operacje ilorazu, kwadratu i pierwiastka
print(f'Iloraz podanych liczb to: {round(num1 / num2, 3)}')
print(f'Kwadrat podanych liczb to: {num1 ** 2} oraz {num2 ** 2}')
print(f'Pierwiastek drugirgo stopnia z podanych liczb to: {round(num1 ** (1 / 2), 3)} oraz {round(num2 ** (1 / 2), 3)}')

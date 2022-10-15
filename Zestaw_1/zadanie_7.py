zakres1 = int(input("Wprowadź pierwszą liczbę: "))
zakres2 = int(input("Wprowadź drugą liczbę: "))
if zakres2 - zakres1 < 20:
    licz = zakres1
    while licz <= zakres2:
        print(licz)
        licz += 1
else:
    srednia = int((zakres1 + zakres2) / 2)
    for i in range(srednia - 3, srednia):
        print(i)
    for i in range(srednia + 1, srednia + 4):
        print(i)

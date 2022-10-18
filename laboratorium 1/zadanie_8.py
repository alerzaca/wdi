size = int(input("Podaj wysokość choinki: "))
left = 0
right = 2
space = size - 1
print(" " * space + "X")
space -= 1
for i in range(size - 1):
    print(" " * space + "*" * left + "o" + "*" * right)
    if i % 2 == 0:
        right += 1
    else:
        left += 1
    buf = right
    right = left + 1
    left = buf
    space -= 1
print(" " * (size - 1) + "U")

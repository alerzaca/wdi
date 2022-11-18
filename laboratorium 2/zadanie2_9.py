
def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: return False
    return True


def half_primes(N):
    primes_list = [i for i in range(N) if is_prime(i)]
    half_list, half_list_dif = [], []
    print(primes_list)

    for i in range(len(primes_list)):
        for j in range(i, len(primes_list)):
            half = primes_list[i] * primes_list[j]

            if primes_list[i] == primes_list[j] and half < N:
                half_list.append(half)
            elif half < N:
                half_list_dif.append(half)

    return [half_list_dif, half_list]


N = int(input("Podaj liczbę N: "))
answer = half_primes(N)

print("Liczby półpierwsze z różnych liczb pierwszych:", answer[0])
print("Liczby półpierwsze z równych liczb pierwszych:", answer[1])

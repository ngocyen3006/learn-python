from math import sqrt, floor


def is_prime(x):
    if x == 0 or x < 0 or x == 1:
        return False

    if x <= 3:
        return True

    upper_bound = floor(sqrt(x))
    for i in range(2, upper_bound + 1):
        if x % i == 0:
            return False

    return True


# https://vi.wikipedia.org/wiki/S%C3%A0ng_Eratosthenes
def list_prime(n):
    if n == 0 or n < 0 or n == 1:
        return []

    arr = []
    upper_bound = floor(sqrt(n))
    for x in range(2, n+1):
        is_prime = True
        for i in arr:
            if i <= (upper_bound + 1) and x % i == 0:
                is_prime = False
                pass

        if is_prime:
            arr.append(x)

    return arr


n = int(input())

print(list_prime(n))

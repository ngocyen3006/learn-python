def divisor(n):
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)
    return arr


n = 11
print(divisor(n))

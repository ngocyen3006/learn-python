def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


a = 149
b = 720
print(gcd(a, b))

# Better Fibonacci

# Method 1
def better_fibonacci(n):
    a = [0, 1, 1]
    if n < 3:
        return a[n]

    for i in range(3, n + 1):
        a.append(a[i - 1] + a[i - 2])
    return a[n]


# Method 2 (copy)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Method 3 (copy)
def fib(n):
    from math import sqrt
    return int((((1 + sqrt(5)) ** n) - ((1 - sqrt(5)) ** n)) / (2 ** n * sqrt(5)))


if __name__ == '__main__':
    testcase = {
        0: 0,
        1: 1,
        3: 2,
        5: 5,
        8: 21,
        10: 55,
        15: 610,
        30: 832040
    }
    for k in testcase:
        print(f"{k} ==> {better_fibonacci(k) == testcase[k]}")
        print(f"{k} ==> {fibonacci(k) == testcase[k]}")
        print(f"{k} ==> {fib(k) == testcase[k]}")
        print("-" * 25)

# Fibonacci

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 5, 6, 8]
    for i in arr:
        print(f"fib({i}) = {fib(i)}")

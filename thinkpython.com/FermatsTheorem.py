# a ** n + b ** n != c ** n if n > 2

def check_fermat(a, b, c, n):
    if (a ** n + b ** n) != c ** n:
        print(r"No, that doesn't work.")
        return
    print("Holy smokes, Fermat was wrong!")


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    n = int(input())

    while n < 3:
        n = int(input())

    check_fermat(a, b, c, n)

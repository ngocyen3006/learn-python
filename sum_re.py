n = int(input())


def sum(n):
    if(n==0):
        return 0
    return n + sum(n-1)


result = sum(n)
print(result)

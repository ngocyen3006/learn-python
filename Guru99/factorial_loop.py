n = int(input())


def fact(n):
    if(n == 0):
        return 1
    
    i = 1
    result = 1
    while (i <= n):
        result = result * i
        i = i + 1
    return result


re = fact(n)
print(re)

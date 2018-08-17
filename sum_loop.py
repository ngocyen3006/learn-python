n = int(input())


def sum(n):
    i = 0
    result = 0
    while(i <= n):
        result = result + i
        i = i + 1
    return result


answer = sum(n)
print(answer)

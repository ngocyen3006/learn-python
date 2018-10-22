# https://www.hackerrank.com/challenges/py-check-subset/problem

result = []
T = int(input())
for i in range(T):
    numberElementA = int(input())
    A = set(map(int, input().split()))
    numberElementB = int(input())
    B = set(map(int, input().split()))
    if A.intersection(B) == A:
        result.append(True)
    else:
        result.append(False)

print('\n'.join(map(str, result)))

# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, input().split()))
n = int(input())
result = []
for i in range(n):
    subset = set(map(int, input().split()))
    if A > subset:
        result.append(True)
    else:
        result.append(False)
print(all(result))

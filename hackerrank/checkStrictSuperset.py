# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = list(map(int, input().split()))
Aset = set(A)
n = int(input())
result = []
for i in range(n):
    subset = set(map(int, input().split()))
    if subset.intersection(Aset) == subset and len(subset) < len(A):
        result.append(True)
    else:
        result.append(False)
print(all(result))

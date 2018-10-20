# https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
E = set(map(int, input().split()))
b = int(input())
F = set(map(int, input().split()))
total = len(E.union(F))
print(total)

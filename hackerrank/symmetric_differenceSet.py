# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
E = set(map(int, input().split()))
b = int(input())
F = set(map(int, input().split()))
total = E.symmetric_difference(F)
print(len(total))

# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
l = set([])
for i in range(n):
    l.add(input())
print(len(l))

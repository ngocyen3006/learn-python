# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
l = []
for i in range(n):
    l.append(input())

print(len(set(l)))

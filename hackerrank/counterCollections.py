# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
size = list(map(int, input().split()))
n = int(input())
count = dict(Counter(size))

price = 0
for i in range(n):
    v = list(map(int, input().split()))
    if v[0] in count.keys() and count[v[0]] > 0:
        price = price + v[1]
        count[v[0]] = count[v[0]] - 1
print(price)

# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import *

n = int(input())
s = input().split()
k = int(input())

a = list(combinations(s, k))
count = 0
for i in range(len(a)):
    if 'a' in a[i]:
        count += 1

print(f"{count/len(a):.3f}")

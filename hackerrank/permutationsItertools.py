# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

s, k = input().split()
k = int(k)
for i in permutations(sorted(s), k):
    print(''.join(i), sep='\n')

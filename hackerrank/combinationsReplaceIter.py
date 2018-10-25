# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

s, k = input().split()
s = sorted(s)
k = int(k)

for j in combinations_with_replacement(s, k):
    print(''.join(j), sep='\n')

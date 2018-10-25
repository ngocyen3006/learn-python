# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

s = input()
print(*[(len(list(g)), int(k)) for k, g in groupby(s)])

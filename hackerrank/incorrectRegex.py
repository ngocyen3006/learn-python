# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

n = int(input())

for i in range(n):
    try:
        re.compile(input())
        print(True)
    except Exception:
        print(False)

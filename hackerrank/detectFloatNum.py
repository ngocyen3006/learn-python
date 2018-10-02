# https://www.hackerrank.com/challenges/introduction-to-regex/problem

regex_pattern = r"^[+|-]?\d{1,}[.]\d{1,}$|^([+|-]?)[.]\d{1,}$"
arr = []

import re
for i in range(0, int(input())):
    fNum = input()
    arr = arr + [bool(re.match(regex_pattern, fNum))]

print("\n".join(map(str, arr)))

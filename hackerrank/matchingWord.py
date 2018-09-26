# https://www.hackerrank.com/challenges/matching-word-non-word/problem

Regex_Pattern = r"^(\w+\W+)+\w{3}$"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

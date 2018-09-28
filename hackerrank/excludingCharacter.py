# https://www.hackerrank.com/challenges/excluding-specific-characters/problem

# Do not delete 'r'.
Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\,|,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

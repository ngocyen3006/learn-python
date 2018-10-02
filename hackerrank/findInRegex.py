# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

Regex_Pattern = r"(?<=[^aeiou])([aeiou]{2,})[^aeiou]"

import re
print("\n".join(re.findall(Regex_Pattern, input(), flags=re.I) or ['-1']))

# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re


def checkRomanNumerals(s):
    if not isinstance(s, str):
        return False
    # thousands = r"M{,3}"
    # hundreds = r"C{1,3}|C[DM]|DC{,3}"
    # tens = r"X{1,3}|X[LC]|LX{,3}]"
    # digits = r"I{1,3}|I[VX]|VI{,3}"
    romanNum = r"^(M{,3})(C[DM]|D?C{,3})(X[LC]|L?X{,3})(I[VX]|V?I{,3})$"
    return bool(re.match(romanNum, s))

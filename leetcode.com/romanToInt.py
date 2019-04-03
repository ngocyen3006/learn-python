# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if s == '':
        return 0

    if len(s) == 1:
        return roman_numerals[s]

    vir_val = roman_numerals[s[1]]
    val = roman_numerals[s[0]]
    if val < vir_val:
        return vir_val - val + romanToInt(s[2:])
    return val + romanToInt(s[1:])


if __name__ == '__main__':
    testcase = {'I': 1,
                'V': 5,
                'III': 3,
                'IV': 4,
                'IX': 9,
                'LVIII': 58,
                'MCMXCIV': 1994,
                'LXXXIX': 89,
                'MMMCMXCIX': 3999,
                'MCDLXXVI': 1476}
    for k in testcase.keys():
        print(f"{k} - {testcase[k]} - {romanToInt(k)} ==> {romanToInt(k) == testcase[k]}")
        print("----------")

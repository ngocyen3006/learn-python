# https://leetcode.com/problems/integer-to-roman/

def intToRoman(num):
    roman_numerals = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    roman_numerals_sub = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

    if num == 0:
        return ''

    if num in roman_numerals.keys():
        return roman_numerals[num]

    if num in roman_numerals_sub.keys():
        return roman_numerals_sub[num]

    if num > 1000:
        return (num // 1000) * 'M' + intToRoman(num % 1000)

    n = len(str(num)) - 1

    if num > 10 ** n and num < 4 * 10 ** n:
        return (num // 10 ** n) * intToRoman(10 ** n) + intToRoman(num % 10 ** n)

    if num > 5 * 10 ** n and num < 9 * 10 ** n:
        return intToRoman(5 * 10 ** n) + intToRoman(num % (5 * 10 ** n))

    return intToRoman((num // 10 ** n) * 10 ** n) + intToRoman(num % 10 ** n)


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
        print(f"{testcase[k]} - {k} - {intToRoman(testcase[k])} ==> {k == intToRoman(testcase[k])}")
        print("----------")

# https://leetcode.com/problems/excel-sheet-column-number/

def titleToNumber(s):
    res = 0
    for c in s:
        res = res * 26 + (ord(c) - ord('A') + 1)
    return res


if __name__ == '__main__':
    testcase = {'A': 1,
                'Z': 26,
                'AB': 28,
                'ZY': 701}
    for k in testcase.keys():
        print(titleToNumber(k) == testcase[k])

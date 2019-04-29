# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/

def convertToTitle(n):
    title = ''
    while n > 0:
        n -= 1
        title = chr((n % 26) + 65) + title
        n = n // 26
    return title


if __name__ == '__main__':
    testcase = {'A': 1,
                'Z': 26,
                'AB': 28,
                'ZY': 701}
    for k in testcase.keys():
        print(convertToTitle(testcase[k]) == k)

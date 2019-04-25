# 38. Count and Say
# https://leetcode.com/problems/count-and-say/

def countAndSay(n):
    s = '1'
    i = 1

    while i < n:
        count = 1
        temp = ''
        cur = s[0]
        for j in range(1, len(s)):
            if s[j] == s[j - 1]:
                count += 1
                continue
            temp += str(count) + cur
            cur = s[j]
            count = 1

        temp += str(count) + cur
        s = temp
        i += 1
    return s


if __name__ == '__main__':
    testcase = {1: '1',
                2: '11',
                3: '21',
                4: '1211',
                5: '111221'}
    for k in testcase:
        print(f"{countAndSay(k)} ? {testcase[k]} ==> {countAndSay(k) == testcase[k]}")

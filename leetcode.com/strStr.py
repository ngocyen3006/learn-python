# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1


def test():
    testcase = [['hello', 'll'], ['aaaaaa', 'bba'], ['a', 'a'], ['a', 'b'], ['aaa', 'aa']]

    for test in testcase:
        print(strStr(test[0], test[1]))


if __name__ == '__main__':
    test()

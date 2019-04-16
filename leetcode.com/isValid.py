# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    if len(s) % 2 == 1:
        return False
    valid_dic = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in valid_dic.keys():
            stack.append(c)
        else:
            if not stack or valid_dic[stack.pop()] != c:
                return False
    return not stack


def test():
    testcase = {
        '(){}[]': True,
        '([)]': False,
        '{[]}': True
    }
    for k in testcase.keys():
        print(isValid(k) == testcase[k])


if __name__ == '__main__':
    test()

# 66. Plus One
# https://leetcode.com/problems/plus-one/

def plusOne(digits):
    rev = digits[::-1]

    if rev[0] + 1 == 10:
        hold = 1
        rev[0] = 0
    else:
        hold = 0
        rev[0] = rev[0] + 1

    if hold == 0:
        return rev[::-1]
    else:
        for i in range(1, len(digits)):
            if rev[i] + hold == 10:
                rev[i] = 0
                hold = 1
            else:
                rev[i] = rev[i] + hold
                hold = 0

    if hold == 1:
        rev.append(1)

    return rev[::-1]


if __name__ == '__main__':
    testcase = [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9, 9, 9, 9], [1, 0, 0, 0, 0])]
    for test in testcase:
        print(plusOne(test[0]))
        print(plusOne(test[0]) == test[1])
        print('-----')

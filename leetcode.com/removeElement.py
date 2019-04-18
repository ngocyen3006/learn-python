# 27. Remove Element
# https://leetcode.com/problems/remove-element/

def removeElement(nums, val):
    if not nums or nums == []:
        return 0
    while nums.count(val) != 0:
        nums.remove(val)
    return len(nums)


def test():
    testcase = [[[3, 2, 2, 3], 3], [[0, 1, 2, 2, 3, 0, 4, 2], 2]]
    for test in testcase:
        print(removeElement(test[0], test[1]))


if __name__ == '__main__':
    test()

# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicate(nums):
    n = len(nums)
    i = 1
    while i < n:
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            n -= 1
        else:
            i += 1
    return len(nums)


def test():
    testcase = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for test in testcase:
        print(removeDuplicate(test))
        print(test)
        print("---")


if __name__ == '__main__':
    test()

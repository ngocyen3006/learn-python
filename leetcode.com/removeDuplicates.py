# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicate(nums):
    if not nums or nums == []:
        return 0
    i = 1
    j = 0
    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1


def test():
    testcase = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for test in testcase:
        print(removeDuplicate(test))
        print(test)
        print("---")


if __name__ == '__main__':
    test()

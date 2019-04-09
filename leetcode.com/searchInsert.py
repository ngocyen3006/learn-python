# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            return mid
    return i


def test():
    nums, target, output = [1, 3, 4, 5, 6], 5, 3
    print(searchInsert(nums, target) == output)
    print('-' * 15)

    nums, target, output = [1, 3, 5, 6], 2, 1
    print(searchInsert(nums, target) == output)
    print('-' * 15)

    nums, target, output = [1, 3, 5, 6], 7, 4
    print(searchInsert(nums, target) == output)
    print('-' * 15)

    nums, target, output = [1, 3, 5, 6], 0, 0
    print(searchInsert(nums, target) == output)
    print('-' * 15)

    nums, target, output = [1, 3], 2, 1
    print(searchInsert(nums, target) == output)
    print('-' * 15)


if __name__ == '__main__':
    test()

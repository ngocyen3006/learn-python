# https://leetcode.com/problems/two-sum/
def twoSum(nums, target):
    for i in range(len(nums)):
        l = [j for j, n in enumerate(nums) if n == target - nums[i]]
        if len(l) == 0 or (len(l) == 1 and i in l):
            continue
        elif len(l) == 1 and l[0] > i:
            return [i, l[0]]
        else:
            return [i, l[1]]


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 9
    print(twoSum(arr, target))
    print("--------------")
    arr = [3, 3]
    target = 6
    print(twoSum(arr, target))
    print("--------------")
    arr = [3, 2, 4]
    target = 6
    print(twoSum(arr, target))
    print("--------------")
    arr = [2, 5, 5, 11]
    target = 10
    print(twoSum(arr, target))

# https://leetcode.com/problems/two-sum/
# Optimized

def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        n = target - nums[i]
        if n in dict.keys():
            return [dict[n], i]
        else:
            dict[nums[i]] = i


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

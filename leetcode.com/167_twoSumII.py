# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Runtime: 36ms (99.39%)
# Memory: 13.6 MB (5.14%)

def twoSum(numbers, target):
    dict = {}
    for i in range(len(numbers)):
        n = target - numbers[i]
        if n in dict.keys():
            return [dict[n] + 1, i + 1]
        else:
            dict[numbers[i]] = i

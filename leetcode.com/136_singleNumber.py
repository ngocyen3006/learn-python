# 136. Single Number
# https://leetcode.com/problems/single-number/

# Runtime: 44ms (68.18%)
# Memory: 14.9 MB (5.05%)

def singleNumber(nums):
    sum_all = sum(nums)
    sum_set = sum(set(nums))
    sum_not_single_nums = sum_all - sum_set
    return sum_set - sum_not_single_nums


# Runtime: 40ms (94.63%)
# Memory: 14.7 MB (5.05%)
def singleNumber2(nums):
    res = 0
    for num in nums:
        res ^= num
        print(res)
    return res


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(singleNumber2(nums))
    print('----')
    nums = [2, 2, 1, 1, 4]
    print(singleNumber2(nums))
    print('----')
    nums = [2, 2, 1, 1, 7, 7, 6, 5, 6]
    print(singleNumber2(nums))

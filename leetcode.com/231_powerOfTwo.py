# 231. Power of Two
# https://leetcode.com/problems/power-of-two/

# Runtime: 36ms (100.00%)
# Memory: 13.3 MB (6.20%)

def isPowerOfTwo(n):
    x = 1
    while x < n:
        x = x << 1
    return x == n

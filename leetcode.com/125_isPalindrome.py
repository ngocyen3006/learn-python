# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# Runtime: 52ms (93.89%)
# Memory: 13.4 MB (39.19%)

def isPalindrome(s):
    s = s.lower()
    c = ''
    for string in s:
        if string.isalnum():
            c += string
    return c == c[::-1]

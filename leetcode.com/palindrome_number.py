# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

def isPalindrome(x):
    if x < 0:
        return False
    y = str(x)[::-1]
    n = int(y)
    return n == x


if __name__ == '__main__':
    a = [121, -121, 10, 12521, 20]
    for e in a:
        print(f"isPalindrome({e}) = {isPalindrome(e)}")

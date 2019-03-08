# https://leetcode.com/problems/palindrome-number/
def isPalindrome(x):
    y = x
    n = 0
    while y > 0:
        n = n * 10 + y % 10
        y = y // 10
    if n == x:
        return True
    return False


if __name__ == '__main__':
    a = [121, -121, 10, 12521, 20]
    for e in a:
        print(f"isPalindrome({e}) = {isPalindrome(e)}")

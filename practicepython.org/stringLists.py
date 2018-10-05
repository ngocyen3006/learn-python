def isPalinrome(s):
    r = ''.join(reversed(s))
    if r == s:
        return True
    else:
        return False


s = "abcd"
result = isPalinrome(s)

if result:
    print("{} is a palindrome.".format(s))
else:
    print("{} is not a palindrome.".format(s))

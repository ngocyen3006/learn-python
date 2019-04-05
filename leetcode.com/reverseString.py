# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    i, j = 0, len(s) - 1
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1


if __name__ == '__main__':
    a = ["h", "e", "l", "l", "o"]
    r_a = ["o", "l", "l", "e", "h"]

    b = ["H", "a", "n", "n", "a", "h"]
    r_b = ["h", "a", "n", "n", "a", "H"]

    reverseString(a)
    print(a == r_a)

    reverseString(b)
    print(b == r_b)

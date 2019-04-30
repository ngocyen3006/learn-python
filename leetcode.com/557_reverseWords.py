# 557. Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverseWords(s):
    res = []
    s = s.split(' ')
    for word in s:
        res.append(word[::-1])
    return ' '.join(res)


if __name__ == '__main__':
    word = "Let's take LeetCode contest"
    reverse = "s'teL ekat edoCteeL tsetnoc"
    print(reverseWords(word))
    print(reverseWords(word) == reverse)

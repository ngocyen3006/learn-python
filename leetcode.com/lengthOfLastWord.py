# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s):
    if not s:
        return 0
    s = s.strip()
    return len(s.split(' ')[-1])

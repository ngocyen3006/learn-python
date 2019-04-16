# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    if not strs or len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    n = len(min(strs, key=len))
    i = 0
    while i < n:
        subset = set([s[i] for s in strs])
        if len(subset) != 1:
            return strs[0][:i]
        i += 1
    return strs[0][:n]


def test():
    i, o = ["flower", "flow", "flight"], "fl"
    print(longestCommonPrefix(i))
    print(longestCommonPrefix(i) == o)

    i, o = ["dog", "racecar", "car"], ""
    print(longestCommonPrefix(i))
    print(longestCommonPrefix(i) == o)


if __name__ == '__main__':
    test()

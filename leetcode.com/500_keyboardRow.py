# 500. Keyboard Row
# https://leetcode.com/problems/keyboard-row/

def findWords(words):
    list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    list2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    list3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    res = []
    for word in words:
        lowerWord = word.lower()
        if lowerWord[0] in list1:
            if all([c in list1 for c in lowerWord[1:]]):
                res.append(word)

        elif lowerWord[0] in list2:
            if all([c in list2 for c in lowerWord[1:]]):
                res.append(word)

        elif lowerWord[0] in list3:
            if all([c in list3 for c in lowerWord[1:]]):
                res.append(word)
        else:
            continue
    return res


if __name__ == '__main__':
    words = ['Hello', 'Alaska', 'Dad', 'Peace']
    print(findWords(words))

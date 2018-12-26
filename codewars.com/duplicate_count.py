# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python


def duplicate_count(text):
    text = text.lower()
    d = {}
    for c in text:
        d.setdefault(c, 0)
        d[c] += 1
    res = 0
    for k in d.keys():
        if d[k] > 1:
            res += 1
    return res

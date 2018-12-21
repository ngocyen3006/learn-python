# https://www.codewars.com/kata/scramblies/train/python

def scramble(s1, s2):
    s = {}
    for i in s1:
        s.setdefault(i, 0)
        s[i] += 1

    l = {}
    for j in s2:
        l.setdefault(j, 0)
        l[j] += 1

    return all([bool(k in s.keys() and l[k] <= s[k]) for k in l.keys()])


# Method 2 on codewars
def scramble1(s1, s2):
    return all(s1.count(x) >= s2.count(x) for x in set(s2))


print(scramble('rkqodlw', 'world'))
print(scramble1('rkqodlw', 'world'))

print(scramble('katas', 'steak'))
print(scramble1('katas', 'steak'))

print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble1('cedewaraaossoqqyt', 'codewars'))

def sortArray(a):  # can use set(a)
    b = []
    for i in range(len(a)):
        if a == []:
            return b
        b.append(min(a))
        a.remove(min(a))
        for k in b:
            while a != [] and k == min(a):
                a.remove(min(a))
    return b


def overlap(a, b):
    a1 = sortArray(a)
    b1 = sortArray(b)
    c = a1 + b1
    return sortArray(c)


a = [1, 5, 3, 4, 1, 6, 2, 1]
b = [9, 10, 8, 5, 7, 6, 2, 11, 14, 2, 2, 3, 4, 9, 8]

print(set(a))

print(set(a).intersection(set(b)))

print(set(a).union(set(b)))

print(overlap(a, b))

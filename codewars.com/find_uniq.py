# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

# Method 1
def find_uniq(arr):
    dict = {}
    for i in arr:
        dict.setdefault(i, 0)
        dict[i] += 1
    for i in dict.keys():
        if dict[i] == 1:
            n = i
    return n  # n: unique integer in the array


# Method 2 on codewars
def find_uniq1(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


if __name__ == '__main__':
    arr = [[1, 1, 1, 2, 1, 1], [0, 0, 0.55, 0, 0], [3, 10, 3, 3, 3]]
    for i in arr:
        print(find_uniq(i))
        print(find_uniq1(i))

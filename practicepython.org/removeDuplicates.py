def removeDuplicates1(arr):
    if arr == [] or arr == None:
        return arr
    return set(arr)


def removeDuplicates2(arr):
    if arr == [] or arr == None:
        return arr
    b = []
    for i in arr:
        if i not in b:
            b.append(i)
        else:
            continue
    return b


arr = [1, 2, 5, 3, 7, 5, 0, 6, 2, 5]
# arr = []

print(removeDuplicates1(arr))
print("\n")
print(removeDuplicates2(arr))

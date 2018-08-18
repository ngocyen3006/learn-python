# arr = list(map(int, input().split()))
# arr = list(input().split())
# arr = range(1, 10)
arr = [1, 2, 3 , 4 , 5]
print(arr)

from functools import reduce


def sumByReduce(arr):
    if arr == None or arr == []:
        return None
    return reduce((lambda x, y: x + y), arr)


print(f"sumByReduce: {sumByReduce(arr)}")


def productByReduce(arr):
    if arr == None or arr == []:
        return None
    return reduce((lambda x, y: x * y), arr)


print(f"productByReduce: {productByReduce(arr)}")


def reverseByReduce(arr):
    if arr == None:
        return None
    return reduce(lambda xs, x: [x] + xs, arr, [])


print(f"reverseByReduce: {reverseByReduce(arr)}")


def joinByReduce(arr, s):
    if arr == None or arr == []:
        return None

    arr_strings = map(str, arr)
    return reduce((lambda acc, x: acc + s + x), arr_strings)


print("joinByReduce: %s" % joinByReduce(arr, ":"))


def filterByReduce(checkMethod, arr):
    if arr == None or arr == []:
        return None

    return reduce((lambda x, y: x + ([y] if checkMethod(y) else [])), arr, [])


print(f"filterByReduce: {filterByReduce(lambda x: x % 2 == 0, arr)}")


def countByReduce(checkMethod, arr):
    if arr == None:
        return None
    return reduce((lambda x, y: x + (1 if checkMethod(y) else 0)), arr, 0)


print(f"countByReduce (odd): {countByReduce(lambda x: x % 2  == 1, arr)}")


def allMatch(test, arr):
    if arr == None or arr == []:
        return None

    return reduce((lambda x, y: x and (y if test(y) else False)), arr, True)


print(f"allMatch(positive): {allMatch(lambda x: x > 0, arr)}")


def anyMatch(test, arr):
    if arr == None or arr == []:
        return None

    return reduce((lambda x, y: x or (y if test(y) else False)), arr, False)


print(f"anyMatch(negative): {anyMatch(lambda x: x < 0, arr)}")


def mapByReduce(mapMethod, arr):
    if arr == None:
        return None
    return reduce(lambda x, y: x + [mapMethod(y)], arr, [])


print(f"mapByReduce: {mapByReduce(lambda x: x ** 3, arr)}")

def find1(arr, number):
    for i in arr:
        if i == number:
            return True
    return False


def find2(arr, number):
    if number in arr:
        return True
    return False


# use binary search (only ordered list)
def binarySearch(arr, number):
    if arr == [] or arr == None:
        return False
    if len(arr) == 1:
        if number == arr[0]:
            return True
    else:
        mid = len(arr) // 2
        if number == arr[mid]:
            return True
        elif number < arr[mid]:
            return binarySearch(arr[:mid], number)
        else:
            return binarySearch(arr[mid:], number)
    return False


import random

if __name__ == "__main__":
    l = sorted(random.sample(range(50), 10))
    print(l)
    a = [5, 10, -1, 8, 17, 30, 27]
    for i in a:
        print(i)
        print(str(find1(l, i)) + " == " + str(find2(l, i)) + " == " + str(binarySearch(l, i)))

# http://www.practicepython.org/exercise/2014/11/11/20-element-search.html

def find1(arr, number):
    """
    Find 1 will search number in the arr by compare it will each single number in arr
    """
    for i in arr:
        if i == number:
            return True
    return False


def find2(arr, number):
    '''
    Use "in" operator to find number in list arr.
    '''
    if number in arr:
        return True
    return False


def binarySearch(arr, number):
    '''
    Use binary search number in list arr (only ordered list).

    :return: True if number is found and False if not found
    '''
    if arr == [] or arr == None:
        return False

    mid = len(arr) // 2
    if number == arr[mid]:
        return True

    if number < arr[mid]:
        return binarySearch(arr[:mid], number)

    return binarySearch(arr[mid + 1:], number)


import random

if __name__ == "__main__":
    arr = sorted(random.sample(range(50), 10))
    print(arr)
    a = [5, 10, -1, 8, 17, 30, 27]
    for i in a:
        print(i)
        print("{} == {} == {}".format(find1(arr, i), find2(arr, i), binarySearch(arr, i)))

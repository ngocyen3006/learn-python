from runtimeFunction import timed


@timed
def binarySearch(arr, x):
    '''
    Search x in sorted array

    :return: index of x in arr if it found, otherwise return -1
    '''
    if arr == [] or arr == None:
        return -1

    mid = len(arr) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        return binarySearch(arr[:mid], x)
    if arr[mid] < x:
        return binarySearch(arr[mid + 1:], x)
    return -1

from runtimeFunction import timed


@timed
def linearSearch(arr, x):
    '''
    Search x in array. If there are multiple return only index of first index in array.

    :return: index of x in arr if it found, otherwise return -1
    '''
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

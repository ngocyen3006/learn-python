import copy


def comma(arr):
    if arr == None or arr == []:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        temp = copy.copy(arr)
        del temp[-1]
        string = "'" + ", ".join(temp) + ", and " + arr[-1] + "'"
        return string


spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
result = comma(spam)
print(result)

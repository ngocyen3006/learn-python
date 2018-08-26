def comma(arr):
    string = "'"
    for i in range(0, len(arr)):
        if i == (len(arr) - 1):
            string = string + 'and ' + arr[-1] + "'."
        else:
            string = string + arr[i] + ", "
    return string


spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
result = comma(spam)
print(result)

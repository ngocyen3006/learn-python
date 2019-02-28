# Find One Missing Number from 1 to 10

def find_missing_number(list_numbers):
    s = list(range(1, 11))
    diff = list(set(s).difference(set(list_numbers)))
    return diff[0]
    # Other method
    # return sum(s) - sum(list_numbers)


if __name__ == '__main__':
    arr = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    print(find_missing_number(arr))

# Numbers and Ranges ...

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"


def find_range(input_list, input_number):
    l = find_index(input_list, input_number, 0)
    return Range(l[0], l[1])


def find_index(input_list, input_number, add_index=0):
    mid = len(input_list) // 2
    i = -1
    j = -1
    m = mid
    while input_list[m - 1] == input_number:
        i = m - 1
        if j == -1 or j > i:
            j = i
        m -= 1

    while input_list[m] == input_number:
        j = m
        if i == -1:
            i = j
        m += 1

    if input_list[mid - 1] > input_number:
        return find_index(input_list[:mid - 1], input_number, add_index)

    if input_list[mid - 1] < input_number:
        add_index += mid
        return find_index(input_list[mid:], input_number, add_index)

    return [i + add_index, j + add_index, add_index]


if __name__ == '__main__':
    a = [1, 1, 2, 3, 3, 5, 7, 8, 8, 15]
    x = 3
    x1 = 7
    x2 = 8
    print(find_range(a, x))
    print("-" * 15)
    print(find_range(a, x1))
    print("-" * 15)
    print(find_range(a, x2))
    print("-" * 15)

# Array Partition

def find_partitions(input_list):
    res = []
    n = input_list[0]
    i = 1
    while i < len(input_list) and input_list[i] == input_list[i - 1] + 1:
        i += 1
    try:
        if n == input_list[i - 1]:
            res.append(n)
        else:
            res.append(str(n) + "-" + str(input_list[i - 1]))
        return res + find_partitions(input_list[i:])
    except IndexError:
        return res


if __name__ == '__main__':
    a = [1, 2, 3, 6, 7, 8, 10, 11]
    r_a = ["1-3", "6-8", "10-11"]
    print(find_partitions(a) == r_a)
    print("-" * 25)

    a = [1, 2, 3, 4, 7, 8, 9]
    r_a = ["1-4", "7-9"]
    print(find_partitions(a) == r_a)
    print("-" * 25)

    a = [1, 3, 7, 8, 9]
    r_a = [1, 3, "7-9"]
    print(find_partitions(a) == r_a)
    print("-" * 25)

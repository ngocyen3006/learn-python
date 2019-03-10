# Max Gain

def max_gain(input_list):
    min_element = input_list[0]
    max_gain = 0
    for e in input_list:
        if e < min_element:
            min_element = e
        else:
            max_gain = max(max_gain, e - min_element)
    return max_gain


if __name__ == '__main__':
    a = [100, 40, 20, 10]
    print(f"{max_gain(a)} = 0 ==> {max_gain(a) == 0}")
    print("-" * 25)

    a = [0, 50, 10, 100, 30]
    print(f"{max_gain(a)} = 100 ==> {max_gain(a) == 100}")
    print("-" * 25)

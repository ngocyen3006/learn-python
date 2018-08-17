def split_and_join(line):
    # write your code here
    line = line.split(" ")
    print(line)
    line = "-".join(line)
    print(line)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

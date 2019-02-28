# Reverse a String

def reverse_string(a_string):
    return a_string[::-1]


if __name__ == '__main__':
    arr = ["", "abcde", "madam", "1"]
    for i in arr:
        print(reverse_string(i))

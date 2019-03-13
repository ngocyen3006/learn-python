# Unique Chars in a String

def unique_chars_in_string(input_string):
    s = set(input_string)
    changed_string = "".join(s)
    return len(input_string) == len(changed_string)


def unique_chars_in_string_2(input_string):
    return len(input_string) == len(set(input_string))


if __name__ == '__main__':
    testcase = {
        "": True,
        "Language": False,
        "Python": True,
        "Programming": False
    }
    i = 0
    for k in testcase:
        print(f"Case {i}: {k} ==> {unique_chars_in_string(k) == testcase[k]}")
        print(f"Case {i}: {k} ==> {unique_chars_in_string_2(k) == testcase[k]}")
        i += 1
        print("-" * 25)

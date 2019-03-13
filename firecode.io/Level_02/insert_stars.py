# Insert stars

def insert_star_between_pairs(a_string):
    if a_string is None:
        return None

    res = a_string
    j = 0
    for i in range(len(a_string) - 1):
        if a_string[i] == a_string[i + 1]:
            res = res[:i + 1 + j] + "*" + res[i + 1 + j:]
            j += 1
    return res


def insert_star_between_pairs_2(a_string):
    if not a_string or len(a_string) == 1:
        return a_string
    if a_string[0] == a_string[1]:
        return insert_star_between_pairs(a_string[0]) + "*" + insert_star_between_pairs(a_string[1:])
    return insert_star_between_pairs(a_string[0]) + insert_star_between_pairs(a_string[1:])


if __name__ == '__main__':
    testcase = {
        "cac": "cac",
        "cc": "c*c",
        "bbb": "b*b*b",
        "abba": "ab*ba",
        "abbba": "ab*b*ba",
        None: None
    }
    i = 1
    for k in testcase:
        print(f"Case {i}: {k} ==> {insert_star_between_pairs(k) == testcase[k]}")
        print(insert_star_between_pairs(k))
        print("---")
        print(f"Case {i}: {k} ==> {insert_star_between_pairs_2(k) == testcase[k]}")
        print(insert_star_between_pairs_2(k))
        print("-" * 25)
        i += 1

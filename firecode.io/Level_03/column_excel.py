# Excel Spreadsheet - Column Name to Number

import string


def excel_column_name_to_number(column_title):
    res = 0
    # letter = " ".join(string.ascii_uppercase).split(" ")
    for c in column_title:
        # res = res * 26 + (letter.index(c) + 1)
        res = res * 26 + (ord(c) - ord('A') + 1)
    return res


if __name__ == '__main__':
    testcase = {
        "A": 1,
        "C": 3,
        "AA": 27,
        "ABCD": 19010,
        "ABCDZ": 494286,
        "AZ": 52,
        "BA": 53
    }

    for k in testcase:
        print(f"{k} ==> {excel_column_name_to_number(k) == testcase[k]}")
        print(excel_column_name_to_number(k))
        print("-" * 25)

    print(26 * 3)
    print(19010 - 26 ** 3)

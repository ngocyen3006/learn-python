# Excel Spreadsheet - Column Number to Column Name

def excel_column_number_to_name(column_number):
    c = ""
    while column_number > 0:
        column_number -= 1
        c = chr((column_number % 26) + 65) + c
        column_number = column_number // 26
    return c


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
        print(f"{testcase[k]} ==> {excel_column_number_to_name(testcase[k]) == k}")
        print(excel_column_number_to_name(testcase[k]))
        print("-" * 25)

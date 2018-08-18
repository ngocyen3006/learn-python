# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    count = 0
    len_sub = len(sub_string)
    # if (len_sub == 1):
    #     for i in range(0, len(string)):
    #         if string[i] == sub_string:
    #             count = count + 1
    #     return count
    for i in range(0, len(string)):
        if(string[i:len(sub_string)+i] == sub_string):
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# Palindrone Tester

def is_palindrome(input_string):
    return input_string == input_string[::-1]


if __name__ == '__main__':
    arr = ["madam", "", "aabb", "race car"]
    for i in arr:
        print(f"is_palindrome({i}) == {is_palindrome(i)}")

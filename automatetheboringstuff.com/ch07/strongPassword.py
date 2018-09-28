import re


def checkPass(password):
    # password is at least eight characters long
    if len(password) < 8:
        return False
    # password must contains at least one uppercase character
    if not any([c.isupper() for c in password]):
        return False
    # password must contains at least one digit
    if not any([c.isdigit() for c in password]):
        return False
    # password must contains at least one lowercase character
    if not any([c.islower() for c in password]):
        return False
    return True


def checkPassRegex(password):
    # password is at least eight characters long
    lenPass = '^(.){8,}$'
    if re.match(lenPass, password) is None:
        return False
    # password must contains at least one uppercase character
    if not bool(re.search('[A-Z]', password)):
        return False
    # password must contains at least one digit
    if not bool(re.search('[0-9]', password)):
        return False
    # password must contains at least one lowercase character
    if not bool(re.search('[a-z]', password)):
        return False
    return True


# Test cases for checkPassword
# Key is input password, and value is the expected output
testCases = {
    "12345": False,  # length is not enough
    "a12345678": False,  # missing upper case
    "A12345678": False,  # missing lower case
    "aaaaAAAA": False,  # missing digit
    "12345678": False,  # missing both upper and lower
    "aaaaaaaaaaa": False,  # missing both upper and digit
    "AAAAAAAAAAA": False,  # missing both lower and digit
    "aA123": False,  # has everything, but length is not enough
    "aA123456": True  # password ok
}

print(testCases)

for password, expect in testCases.items():
    # Actual result after run the function against input
    actual = checkPassRegex(password)
    # Verify if the function checkPassword return expected result
    testPassed = actual == expect
    print("checkPassword({}) == {}, expect {} --> Test case result: {}".format(password,
                                                                               actual, expect, testPassed))

# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def reverseString(s):
    string = s.split()
    return " ".join(reversed(string))


TestCases = {
    "My name is John": "John is name My",
    "12345": "12345",
    "I am a student": "student a am I",
    "": "",
    "1 2 3": "3 2 1"
}
for k, v in TestCases.items():
    actual = reverseString(k)
    test_result = actual == v
    print("reverseString({}) == {}, expect {} "
          "\n--> Test case result: {}".format(k, actual, v, test_result))

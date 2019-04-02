# https://leetcode.com/problems/to-lower-case/

def toLowerCase(str):
    return str.lower()


if __name__ == '__main__':
    a = ['Hello', 'hello', 'HELLO', 'heLLo']

    for e in a:
        print(toLowerCase(e))

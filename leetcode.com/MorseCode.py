# https://leetcode.com/problems/unique-morse-code-words/

from pprint import pprint


def uniqueMorseRepresentations(words):
    dict_morse_code = store_Morse_code()
    code = []
    for w in words:
        Morse_code = ''
        for c in w:
            Morse_code += dict_morse_code[c]
        if Morse_code not in code:
            code.append(Morse_code)
    return len(code)


def store_Morse_code():
    Morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    dict_Morse_code = {}
    a = 97
    for c in Morse_code:
        dict_Morse_code[chr(a)] = c
        a += 1
    return dict_Morse_code


if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    print(uniqueMorseRepresentations(words))

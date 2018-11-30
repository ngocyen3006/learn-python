# https://www.codewars.com/kata/create-phone-number/train/python

def create_phone_number(n):
    s = ""
    for i in n:
        s = s + str(i)
    return "({}) {}-{}".format(s[:3],s[3:6],s[6:])

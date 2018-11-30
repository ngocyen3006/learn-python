# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

def openOrSenior(data):
    res = []
    for element in data:
        if element[0] >= 55 and element[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res

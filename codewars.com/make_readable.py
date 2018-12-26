# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    h = int(seconds / 3600)
    seconds = seconds - h * 3600
    m = int(seconds / 60)
    seconds = seconds - m * 60
    # return f"{h:02d}:{m:02d}:{seconds:02d}"
    return "{:02d}:{:02d}:{:02d}".format(h, m, seconds)


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))

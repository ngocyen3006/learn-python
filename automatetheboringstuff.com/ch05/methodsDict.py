spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print("A value of spam: ", v)

print("".rjust(20, "-"))

for k in spam.keys():
    print("A key of spam: ", k)

print("".rjust(20, "-"))

print("Keys of spam: ", spam.keys())

print("".rjust(20, "-"))

print("List keys of spam: ", list(spam.keys()))

print("".rjust(20, "-"))

for i in spam.items():
    print("Item of spam: ", i)

print("".rjust(20, "-"))

for k, v in spam.items():
    print("Key: " + k + " Value: " + str(v))

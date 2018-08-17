# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

print("-------------------------------")
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

print("-------------------------------")
# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


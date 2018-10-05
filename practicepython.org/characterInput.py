import datetime

print("Give me your name: ")
name = input()
print("Enter your age: ")
age = int(input())

currentYear = datetime.date.today().year
yearToHundredAge = currentYear + (100 - age)
print("%s will be 100 years old in the year %d." % (name, yearToHundredAge))
